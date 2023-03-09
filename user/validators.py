import datetime

from dateutil.relativedelta import relativedelta
from rest_framework.exceptions import ValidationError


def check_birth_date(birth_date):
    year_diff = relativedelta(datetime.date.today(), birth_date).years

    if year_diff < 9:
        raise ValidationError("Людям младше 9 лет нельзя создавать оюъявления.")

def check_email(email):
    if "rambler.ru" in email.split("@")[-1]:
        raise ValidationError("Регистрация с домена rambler.ru запрещена.")