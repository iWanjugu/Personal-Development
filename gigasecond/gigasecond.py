# GIGASECOND ANNIVERSARY
# LANGUAGE: PYTHON

# Write a function that will calculate the date that someone will celebrate their 1 gigasecond anniversary.

# Note: A gigasecond is one billion (10**9) seconds.

# The input is three parameters representing someone's birthday.

# As a convenience for celebration planning, the function should also calculate the day of the week and the number of days from today.

# The output should be an array formatted as such: ["YYYY-MM-DD", 'day_of_the_week', days_until]

# You can google datetime in python to familiarize yourself with it


# Examples:

# gigasecond(1988, 5, 15) # ["2020-01-22", "Wednesday", "1764 days left"]
# gigasecond(2015, 2, 17) # ["2046-10-26", "Friday", "11538 days left"]

##################################################################################

#datetime function
from datetime import datetime
# from datetime import timedelta

# import readline
import time
import datetime

### BIRTH DATE
# #Getting Birth Date details
# birth_year = input('Enter your year of birth. (Format [yyyy]): ')
# birth_month = input('Enter your month of birth. (Format [mm]): ')
# birth_day = input('Enter your day of birth. (Format [dd]): ')
# birth_date = (birth_day, birth_month, birth_year)
#
# print (birth_date)

birth_year = 1988
birth_month = 8
birth_day = 19

birth_date = str("19/8/1988")
print (birth_date)

now = datetime.date(2015, 9, 29)
gigasecond = 10**9
difference = datetime.timedelta(seconds=10**9)

gig_anniversery = birth_date + difference

# day_of_week =

days_remaining = gig_anniversery - now

### TODAY DATE
#Getting today's details'
today_date = datetime.date.today()
current_year = today_date.year #takes the year from the 'today_date' variable
current_month = today_date.month
current_day = today_date.day

today_time = today_date.timetuple()
current_hour = today_time.tm_hour
current_minute = today_time.tm_min
current_second = today_time.tm_sec

print(today_time)
print(today_date.ctime())


# today_date_info = '%d/%d/%d/%d/%d/%d' %(current_day, current_month, current_year, current_hour, current_minute, current_second)
# print(today_date_info)


#print '%d/ %d/ %d' %(current_year, current_month, current_day)


print (current_year)
print (current_month)
print (current_day)
print (current_hour)
print (current_minute)
print (current_second)





# today = str(datetime.now())
#
# today_date = '%d/%d/%d' %(current_day, current_month, current_year)
# print (today_date)
#
# today_date_int = datetime.datetime(time.strptime(birth_date, "%d/%m/%Y"))
# print (today_date_int)
# print (time.strptime(today_date, "%d/%m/%Y"))
#
# int(today_date) - int(birth_date)
#
# #Parsing Dates and Times from Strings



# #Gigasecond conversions
# gigasecond = 10**9
# year_in_sec = (365.25*24*60*60)
#
# #number of years in a gigasecond
# gig_year = gigasecond/year_in_sec
#
# print (gigasecond)
# print (year_in_sec)
# print (gig_year)
