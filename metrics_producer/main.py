import concurrent
from concurrent import futures
import time

import configs
from kafka_producer import send_to_kafka
from metrics_producer import log
from multithread_monitor import get_site_metrics


def get_metrics_and_send(site: dict) -> None:
    url = site["url"]
    log.info("Get metrics for site " + url)
    metrics = get_site_metrics(url, site["regex"])
    if metrics:
        send_to_kafka(metrics)


def main():
    sites = configs.sites
    with concurrent.futures.ThreadPoolExecutor(max_workers=configs.kafka["producer_concurrency"]) as executor:
        while True:
            executor.map(get_metrics_and_send, sites, timeout=configs.metrics_poll_interval)
            time.sleep(configs.metrics_poll_interval)


if __name__ == "__main__":
    main()
