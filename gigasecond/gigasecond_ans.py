__author__ = 'iWanjugu'

from datetime import date,timedelta
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def get_user_b_date(year,month,day):
   giga_birthsecond = date(year, month, day) + timedelta(seconds=1000000000)
   birthday = WEEKDAYS[giga_birthsecond.weekday()]
   days_left = (giga_birthsecond - date.today()).days
   print(giga_birthsecond, birthday, days_left, "days left")
print(get_user_b_date(1992,8,31))