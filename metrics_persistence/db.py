# import psycopg2
# from psycopg2.extras import DictCursor
#
# import configs
#
# # conn = psycopg2.connect(configs.db_connection_string)
#
# postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(1, 25, configs.db_connection_string)
#
# insert_query = """ INSERT INTO item (item_Id, item_name, purchase_time, price) VALUES (%s, %s, %s, %s)"""
#
#
# def write_to_db(data):
#     ps_connection = postgreSQL_pool.getconn()
#     with ps_connection.cursor(cursor_factory=DictCursor) as cursor:
#         cursor.execute(
#             SQL(
#                 "INSERT INTO {} VALUES (%(url_id)s, %(ts)s, %(status)s, %(latency)s)"
#             ).format(Identifier("status")),
#             {
#                 "url_id": url_id,
#                 "ts": payload["check_time"],
#                 "status": payload["status"],
#                 "latency": payload["latency"],
#             },
#         )
#     postgreSQL_pool.putconn(ps_connection)
#
#     except(Exception, psycopg2.DatabaseError) as error:
#     print("Error while connecting to PostgreSQL", error)
#
# finally:
#     # closing database connection.
#     # use closeall() method to close all the active connection if you want to turn of the application
#     if threaded_postgreSQL_pool:
#         threaded_postgreSQL_pool.closeall
#     print("Threaded PostgreSQL connection pool is closed")
#
