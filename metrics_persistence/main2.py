# import psycopg2
# import configs
# from psycopg2 import pool
#
#
# def main():
#     # conn = psycopg2.connect(configs.db_connection_string)
#     postgreSQL_pool = psycopg2.pool.ThreadedConnectionPool(1, 25, configs.db_connection_string)
#
#     if (postgreSQL_pool):
#         print("Connection pool created successfully")
#
#     ps_connection = postgreSQL_pool.getconn()
#
#     query_sql = 'SELECT VERSION()'
#
#     cur = ps_connection.cursor()
#     cur.execute(query_sql)
#
#     version = cur.fetchone()[0]
#     print(version)
#
#
# if __name__ == "__main__":
#     main()