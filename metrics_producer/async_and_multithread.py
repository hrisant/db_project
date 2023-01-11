# import asyncio
# import requests
#
#
# if regex:
#             try:
#                 payload["regex_match"] = bool(re.search(regex, response.text))
#             except re.error as e:
#                 raise e
#
# self.producer.produce(
#                 self.topic,
#                 value=json.dumps(payload, cls=JSONDatetimeEncoder),
#                 callback=_log_produced,
#             )
#             self.producer.poll(1)
#         except KafkaException as e:
#             self.logger.error(
#                 "An error occurred while producing a message: %s", e.args[0].reason
#             )
#
# class JSONDatetimeEncoder(json.JSONEncoder):
#     """JSON encoder with datetime serialization capabilities.
#     Serializes `datetime.datetime` types as their `isoformat` representation
#     and `datetime.timedelta` types as their `total_seconds` representation.
#     """
#
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         if isinstance(obj, timedelta):
#             return obj.total_seconds()
#         return super(JSONDatetimeEncoder, self).default(obj)
#
# thread_local = threading.local()
#
# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session
#
# def get_site_metrics(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")
# async def main():
#     loop = asyncio.get_event_loop()
#     future1 = loop.run_in_executor(None, requests.get, 'http://www.google.com')
#     future2 = loop.run_in_executor(None, requests.get, 'http://www.google.co.uk')
#     response1 = await future1
#     response2 = await future2
#     print(response1.text)
#     print(response2.text)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())