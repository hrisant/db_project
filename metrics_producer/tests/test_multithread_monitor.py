from pytest_httpserver import HTTPServer

from metrics_producer.multithread_monitor import get_site_metrics


def test_get_site_metrics_with_regex(httpserver: HTTPServer):
    httpserver.expect_request("/foobar", method="GET").respond_with_data("foo bar", content_type="text/plain")
    metrics = get_site_metrics(httpserver.url_for("/foobar"), "bar")
    print(metrics)
    assert(isinstance(metrics["url"], str))
    assert(isinstance(metrics["response_time"], int))
    assert(metrics["status_code"] == 200)
    assert(metrics["regex"] == "bar")
    assert(metrics["regex_found"])


def test_get_site_metrics_without_regex(httpserver: HTTPServer):
    httpserver.expect_request("/foobar", method="GET").respond_with_data("foo bar", content_type="text/plain")
    metrics = get_site_metrics(httpserver.url_for("/foobar"))
    print(metrics)
    assert(isinstance(metrics["url"], str))
    assert(isinstance(metrics["response_time"], int))
    assert(metrics["status_code"] == 200)
    assert(metrics["regex"] is None)
    assert(metrics["regex_found"] is False)


def test_get_site_metrics_wrong_url(httpserver: HTTPServer):
    httpserver.expect_request("/foobar", method="GET").respond_with_data("foo bar", content_type="text/plain")
    metrics = get_site_metrics(httpserver.url_for("/aaa"))
    assert (isinstance(metrics["url"], str))
    assert (isinstance(metrics["response_time"], int))
    # sadly it does not return 404 as one woul;d expect but 500
    assert (metrics["status_code"] != 200)
    assert (metrics["regex"] is None)
    assert (metrics["regex_found"] is False)


def test_get_site_metrics_wrong_http_method(httpserver: HTTPServer):
    httpserver.expect_request("/foobar", method="POST").respond_with_data("foo bar", content_type="text/plain")
    metrics = get_site_metrics(httpserver.url_for("/foobar"))
    assert (isinstance(metrics["url"], str))
    assert (isinstance(metrics["response_time"], int))
    assert (metrics["status_code"] != 200)
    assert (metrics["regex"] is None)
    assert (metrics["regex_found"] is False)


def test_get_site_metrics_wrong_url_schema(caplog):
    url_with_wrong_schema = "h://gg.c"
    expected_error_message = "Exception while getting metrics from site {}".format(url_with_wrong_schema)
    expected_exception_name = "requests.exceptions.InvalidSchema"
    metrics = get_site_metrics(url_with_wrong_schema)
    assert (caplog.records[0].levelname == "ERROR")
    assert (expected_error_message in caplog.text)
    assert ('requests.exceptions.InvalidSchema' in caplog.text)
    assert(not metrics)


def test_get_site_metrics_wrong_url_type(caplog):
    metrics = get_site_metrics(3.14)
    assert (caplog.records[0].levelname == "ERROR")
    assert ('requests.exceptions.MissingSchema' in caplog.text)
    assert(not metrics)

