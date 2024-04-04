import datetime

def format_date(input_date):
    date_obj = datetime.datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

def mask_card1(card_number: str) -> str:
    if len(card_number) == 16:  # Проверяем длину номера карты
        masked_card1 = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
        return masked_card1
    return "Некорректный номер карты"

def mask_account1(account_number: str) -> str:
    if len(account_number) > 4:  # Проверяем, что номер счета хотя бы 4 символа
        masked_account1 = '**' + account_number[-4:]
        return masked_account1
    return "Некорректный номер счета"