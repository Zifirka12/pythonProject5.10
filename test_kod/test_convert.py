from datetime import datetime
from src.widget import mask_number, convert_date_format


# Проверка функции mask_number()
def test_mask_number():
    assert mask_number("Visa 1234567890123456") == "Visa 1234 56** **** 3456"
    assert mask_number("Maestro 9876543210987654") == "Maestro 9876 54** **** 7654"
    assert mask_number("Счет 73654108430135874305  ") == "Счет **4305"
    assert mask_number("Some_Text_123456") == "Some_Text_123456"
    return "Тест test_mask_number успешно пройден"


# Проверка функции convert_date_format()
def test_convert_date_format():
    assert convert_date_format("2018-07-11T02:26:18.671407") == "11.07.2018"
    assert convert_date_format("2023-12-31T23:59:59.999999") == "31.12.2023"
    return "Тест test_mask_account успешно пройден"


if __name__ == "__main__":
    if all([test_mask_number() == "Тест test_mask_number успешно пройден",
            test_convert_date_format() == "Тест test_convert_date_format успешно пройден"]):
        print("Все тесты успешно пройдены.")