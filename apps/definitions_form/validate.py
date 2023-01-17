import datetime, re


def validate_date(date):
    date_format = '%Y-%m-%d'

    try:
        dateObject = datetime.datetime.strptime(date, date_format)
        print(dateObject)
        return bool(dateObject)

    except ValueError:
        return "Incorrect data format, should be YYYY-MM-DD"


def validate_phone(phone):
    phone_format = re.match(r'(\+7)[\s]*\d{3}[\s]*\d{3}[\s]?\d{2}[\s]?\d{2}', phone)
    if phone_format:
        return True
    else:
        return "Incorrect data format, should be +7 xxx xxx xx xx"


def validate_email(email):
    email_format = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(email_format, email):
        return True
    else:
        return "Incorrect data format email"