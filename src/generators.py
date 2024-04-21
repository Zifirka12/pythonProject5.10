from typing import List, Generator, Any


def transaction_descriptions(transactions: List[dict]) -> Generator[str, None, None]:
    for transaction in transactions:
        yield transaction["description"]


# Пример вызова функции

transactions = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"},
    {"id": 3, "description": "Перевод со счета на счет"},
    {"id": 4, "description": "Перевод с карты на карту"},
    {"id": 5, "description": "Перевод организации"},
]

descriptions = transaction_descriptions(transactions)

for _ in range(5):
    print(next(descriptions))


def filter_by_currency(transactions: List[dict], currency: str) -> Generator[Any, None, None]:
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {}).get("currency", {}).get("code")
            == currency
        ):
            yield transaction


# Пример вызова функции
transactions = [
    {"id": 939719570, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    {"id": 142264268, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
    {"id": 873106923, "operationAmount": {"currency": {"name": "RUB", "code": "RUB"}}},
    {"id": 895315941, "operationAmount": {"currency": {"name": "USD", "code": "USD"}}},
]

usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions)["id"])
"""
Этот код реализует функцию `filter_by_currency`, которая фильтрует операции в
 списке `transactions` по заданной валюте и возвращает итератор с этими операциями.
  Далее, в примере использования,выводятся идентификаторы двух операций с валютой "USD".
  """


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    for i in range(start, end + 1):
        yield "{:04d} {:04d} {:04d} {:04d}".format(*(int(d) for d in str(i).zfill(16)))


# Пример использования генератора для номеров карт
for card_number in card_number_generator(1, 5):
    print(card_number)
