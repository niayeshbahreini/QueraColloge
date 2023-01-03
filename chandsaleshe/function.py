
from datetime import datetime

def day_calculator(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    sajad_birthday = datetime.strptime('1999-01-14', '%Y-%m-%d')
    days = (date - sajad_birthday).days
    if days > 0:
        return days
    return 'Not yet born'


print(day_calculator('2019-10-19'))
