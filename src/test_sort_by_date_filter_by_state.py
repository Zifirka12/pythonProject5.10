from datetime import datetime
from typing import List, Dict

def sort_by_date(list_of_dicts: List[Dict], order: str = "descending") -> List[Dict]:
    reverse = order == "descending"
    return sorted(list_of_dicts, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)

# Проверка функции sort_by_date()
input_data_sort = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]

# Проверка функции filter_by_state()
def filter_by_state(list_of_dicts: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    return [item for item in list_of_dicts if item.get("state") == state]

input_data_filter = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]

output_default = filter_by_state(input_data_filter, "EXECUTED")
output_canceled = filter_by_state(input_data_filter, "CANCELED")

assert output_default == [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
]

assert output_canceled == [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]

print("Все тесты пройдены успешно.")
