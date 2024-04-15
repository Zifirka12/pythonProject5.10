from src.masks import mask_account, mask_card


# Проверка функции mask_card() с аннотациями типов
def test_mask_card() -> str:
    assert mask_card("1234567890123456") == "1234 56** **** 3456"
    assert mask_card("12345") == "Некорректный номер карты"
    return "Тест test_mask_card успешно пройден"


# Проверка функции mask_account() с аннотациями типов
def test_mask_account() -> str:
    assert mask_account("73654108430135874305") == "**4305"
    assert mask_account("123") == "Некорректный номер счета"
    return "Тест test_mask_account успешно пройден"


if __name__ == "__main__":
    if all([test_mask_card() == "Тест test_mask_card успешно пройден",
            test_mask_account() == "Тест test_mask_account успешно пройден"]):
        print("Все тесты успешно пройдены.")
