# from kafka import KafkaConsumer
# import configs
# import json
#
#
# HOST = configs.kafka["host"]
# SSL_PORT = configs.kafka["port"]
# CONSUMER_GROUP_ID = "group_one"
#
# consumer = KafkaConsumer(
#     configs.kafka["topic"],
#     auto_offset_reset="START_FROM",
#     bootstrap_servers=f"{HOST}:{SSL_PORT}",
#     # client_id = CONSUMER_CLIENT_ID,
#     group_id = CONSUMER_GROUP_ID,
#     security_protocol="SSL",
#     ssl_cafile="ca.pem",
#     ssl_certfile="service.cert",
#     ssl_keyfile="service.key",
#     value_deserializer=lambda m: json.loads(m.decode('ascii'))
# )
#
#
# consumer.
#
# with ThreadPoolExecutor(
#         max_workers=self.batch_size + 10 - (self.batch_size % 10)
# ) as executor:
#     while self.RUNNING:
#         message = self.consumer.poll()
#
#         # Commit before processing for an "at most once" delivery strategy.
#         self.consumer.commit(asynchronous=False)
#         executor.submit(self.write, message)
#
