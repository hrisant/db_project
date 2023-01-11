import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from metrics_producer import configs
from metrics_producer import log

HOST = configs.kafka["host"]
SSL_PORT = configs.kafka["port"]

producer = KafkaProducer(
    bootstrap_servers=f"{HOST}:{SSL_PORT}",
    security_protocol="SSL",
    ssl_cafile="kafka_creds/ca.pem",
    ssl_certfile="kafka_creds/service.cert",
    ssl_keyfile="kafka_creds/service.key",
)


def send_to_kafka(message):
    try:
        message = json.dumps(message).encode('ascii')
        future = producer.send(configs.kafka["topic"], message)
        record_metadata = future.get(timeout=configs.kafka["producer_timeout"])
    except (KafkaError, Exception) as e:
        # Decide what to do if produce request failed...
        log.error("Failed to send message to kafka %s", message)
