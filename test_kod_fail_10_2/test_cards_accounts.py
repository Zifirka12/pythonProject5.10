from src.masks import mask_account, mask_card

# Проверка функции mask_card()
assert mask_card("1234567890123456") == "1234 56** **** 3456"
assert mask_card("12345") == "Некорректный номер карты"

# Проверка функции mask_account()
assert mask_account("73654108430135874305") == "**4305"
assert mask_account("123") == "Некорректный номер счета"

print("Все тесты пройдены успешно.")

