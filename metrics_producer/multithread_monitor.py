import re
import threading
from datetime import datetime

import requests

from metrics_producer import log

thread_local = threading.local()


def get_session() -> requests.Session:
    log.debug("Get session: ", thread_local)
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def get_site_metrics(url: str, regex=None) -> dict:
    site_metrics = {}
    session = get_session()
    try:
        with session.get(url) as response:
            site_metrics = {
                "timestamp": datetime.utcnow().strftime('%Y %b %d - %H:%M:%S'),
                "url": url,
                "response_time": response.elapsed.microseconds,
                "status_code": response.status_code,
                "regex": regex,
                "regex_found": False
            }
            if regex is not None:
                site_metrics["regex_found"] = bool(re.search(regex, response.text))
        log.debug("Collected metrics: ", site_metrics)
    except requests.exceptions.RequestException as e:
        log.exception("Exception while getting metrics from site %s", url)
    return site_metrics
