# Exercise 2
from datetime import date, timedelta


def every_week(start):
    delta = timedelta(days=7)
    while True:
        yield start
        start += delta


start_date = date(2022, 1, 3)       # Monday
weekly_appointment = every_week(start_date)

print(next(weekly_appointment))     # datetime.date(2022, 1, 3)
print(next(weekly_appointment))     # datetime.date(2022, 1, 10)
print(next(weekly_appointment))     # datetime.date(2022, 1, 17)
