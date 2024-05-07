import json
import os
from pathlib import Path
from unittest.mock import Mock, patch

import requests
from dotenv import load_dotenv

from src.utils import get_transaction_rub, read_transactions

load_dotenv()
API_KEY = os.getenv("api_key")


@patch("requests.get")
def test_get_transaction_rub_api_error(mock_get: Mock) -> None:
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.RequestException
    mock_get.return_value = mock_response
    result = get_transaction_rub("USD")
    assert result == 1.0


def test_read_transactions_success() -> None:
    test_data = [{"amount": 100, "currency": "RUB"}]
    with open("test_transactions.json", "w") as f:
        json.dump(test_data, f)

    result = read_transactions(Path("test_transactions.json"))
    assert result == test_data

    os.remove("test_transactions.json")


def test_read_transactions_empty_file() -> None:
    with open("test_transactions.json", "w") as f:
        pass  # Создаём пустой файл

    result = read_transactions(Path("test_transactions.json"))
    assert result == []

    os.remove("test_transactions.json")
