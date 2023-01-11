import concurrent.futures
import json
import logging
import traceback
from datetime import datetime

import psycopg2
from kafka import KafkaConsumer
from psycopg2 import pool
from psycopg2.extras import DictCursor
from psycopg2.sql import SQL

import configs
from metrics_persistence import log

HOST = configs.kafka["host"]
SSL_PORT = configs.kafka["port"]

consumer = KafkaConsumer(
    configs.kafka["topic"],
    # auto_offset_reset=None,
    bootstrap_servers=f"{HOST}:{SSL_PORT}",
    # client_id = CONSUMER_CLIENT_ID,
    group_id=configs.kafka["CONSUMER_GROUP_ID"],
    security_protocol="SSL",
    ssl_cafile="kafka_creds/ca.pem",
    ssl_certfile="kafka_creds/service.cert",
    ssl_keyfile="kafka_creds/service.key",
    value_deserializer=lambda m: json.loads(m.decode('ascii'))
)

insert_query = """ INSERT INTO metrics (logdate, url, resp_code, resp_time, has_regex, regex) VALUES (%s, %s, %s, %s, %s, %s)"""


def persist_to_db(data, postgreSQL_pool):
    log.debug("")
    try:
        ps_connection = postgreSQL_pool.getconn()
        record_to_insert = (data["timestamp"], data["url"], data["status_code"],
                            data["response_time"], data["regex_found"], data["regex"])
        with ps_connection.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(
                SQL(insert_query), record_to_insert)
            ps_connection.commit()
        postgreSQL_pool.putconn(ps_connection)
    except psycopg2.DatabaseError:
        log.exception("Error persisting message %s to db", data)
    finally:
        postgreSQL_pool.putconn(ps_connection)


def main():
    try:
        postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(configs.persistence_concurrency, 25, configs.db_connection_string)

        for msg in consumer:
            log.debug("Message received from kafka %s", msg.value)
            # convert back the timestamp to datetime
            msg.value["timestamp"] = datetime.strptime(msg.value["timestamp"], configs.time_format)
            with concurrent.futures.ThreadPoolExecutor(max_workers=configs.persistence_concurrency) as executor:
                executor.submit(persist_to_db, msg.value, postgreSQL_pool)
    except Exception:
        log.exception("Error  in main")
    finally:
        if postgreSQL_pool:
            postgreSQL_pool.closeall()


if __name__ == "__main__":
    main()
