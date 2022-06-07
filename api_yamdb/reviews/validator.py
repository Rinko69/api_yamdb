from datetime import date
from django.core.exceptions import ValidationError


def no_future(value):
    year = date.today().year
    if value > year:
        raise ValidationError(f'Год не может быть больше текущего {year} года')