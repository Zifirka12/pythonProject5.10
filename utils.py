import json
from typing import List, Dict, Union, Any
import requests


def read_transactions(operations: str) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    try:
        with open(operations, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def get_transaction_rub(transaction: Dict[str, Union[str, float]]) -> Any:
    """
    Возвращает сумму транзакции в рублях.

    Args:
        transaction: Словарь с данными о транзакции.

    Returns:
        Сумма транзакции в рублях (float).
    """
    amount = transaction["amount"]
    currency = transaction.get("currency", "RUB")
    api_key = "zreg2uCOFNUBn4Or2wvNJ1VlpSF22ByN"  # API ключ

    if currency != "RUB":
        """ Получение курса валют с exchangeratesapi.io"""
        response = requests.get(
            (
                "https://api.apilayer.com/exchangerates_data/latest"
                f"?access_key={api_key}&base=RUB&symbols={currency}"
            )
        )

        data = response.json()
        if data.get("success", False):  # Проверка наличия и значения ключа
            rate = data["rates"][currency]
            amount *= rate
        else:
            print(f"Ошибка API: {data.get('error', 'Неизвестная ошибка')}")
            return amount  # Возвращаем исходную сумму

    return amount
