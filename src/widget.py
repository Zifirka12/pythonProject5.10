from datetime import datetime


def mask_card_number(card_number):
    return card_number[:7] + ' **** ' + card_number[-4:]


def mask_account_number(account_number):
    return '**' + account_number[-4:]


def mask_number(input_str):
    split_str = input_str.split()
    if split_str[0] in ['Visa', 'MasterCard', 'Maestro']:
        return ' '.join([split_str[0], mask_card_number(''.join(split_str[1]))])
    elif split_str[0] == 'Счет':
        return 'Счет ' + mask_account_number(split_str[1])


def convert_date_format(input_str):
    input_date = datetime.strptime(input_str, "%Y-%m-%dT%H:%M:%S.%f")
    return input_date.strftime("%d.%m.%Y")


# Пример использования
card_number = input("Введите номер карты: ")
masked_card = mask_number(card_number)
print(masked_card)  # Выведет маскированный номер карты

account_number = input("Введите номер счета: ")
masked_account = mask_number(account_number)
print(masked_account)  # Выведет маскированный номер счета

date_str = input("Введите дату: ")  # "2018-07-11T02:26:18.671407"
print(convert_date_format(date_str))  # 11.07.2018
