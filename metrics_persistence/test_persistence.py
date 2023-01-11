import concurrent.futures
import json
from datetime import datetime
from unittest.mock import MagicMock, patch
import psycopg2
import pytest

from kafka import KafkaConsumer
from psycopg2 import pool
from psycopg2.extras import DictCursor
from psycopg2.sql import SQL

from metrics_persistence import configs
from metrics_persistence import log

from metrics_persistence.main import persist_to_db, main

@pytest.fixture
def mock_pool():
    with patch("psycopg2.pool.ThreadedConnectionPool") as pool:
        yield pool

def test_persist_to_db(mock_pool):
    mock_pool.return_value.getconn.return_value.__enter__.return_value = MagicMock()
    data = {"timestamp": "2020-09-29T16:00:00.000000Z", "url": "test.com", "status_code": 200, "response_time": 0.1, "regex_found": False, "regex": ""}

    persist_to_db(data, mock_pool)

    mock_pool.return_value.getconn.return_value.cursor().execute.assert_called_once()
    mock_pool.return_value.putconn.assert_called_once()

def test_main(mock_pool):
    with patch("concurrent.futures.ThreadPoolExecutor") as executor:
        executor.submit = MagicMock()
        msg = MagicMock()
        msg.value = {"timestamp": "2020-09-29T16:00:00.000000Z", "url": "test.com", "status_code": 200, "response_time": 0.1, "regex_found": False, "regex": ""}
        with patch("metrics_persistence.consumer") as consumer:
            consumer.__iter__.return_value = [msg]
            main()
            executor.submit.assert_called_once()
    mock_pool.return_value.closeall.assert_called_once()
