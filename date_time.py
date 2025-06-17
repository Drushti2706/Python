import datetime
import calendar

def dayFind(date):
    born = datetime.datetime.strptime(date, '%d %m %Y')
    day = born.weekday()
    return calendar.day_name[day]

date = input('Please Enter DOB (dd mm yyyy): ')
print("Day of the week is:", dayFind(date))
