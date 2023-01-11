
# metrics_poll_interval = 300
metrics_poll_interval = 10  # for debug, remove ater
metrics_concurrency = 10
sites = [
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "https://www.google.com", "regex": "google"},
    {"url": "http://www.toyota.ro", "regex": "proprietari"},
     ]
kafka = {
    "host": "kafka-3c56ab9f-indarkwedwell39-82be.aivencloud.com",
    "port": "19269",
    "topic": "default_topic",
    "producer_concurrency": 5,
    "producer_timeout": 3
}

