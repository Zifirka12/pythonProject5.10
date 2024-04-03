import datetime

def format_date(input_date):
    date_obj = datetime.datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")

