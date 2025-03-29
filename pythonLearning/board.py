# String count a string occurrence in a string
import calendar
from calendar import month

def display_calendar():
  year = int(input("Enter year: "))
  month = int(input("Enter month (1-12): "))

  cal = calendar.TextCalendar(calendar.SUNDAY)
  month_calender = cal.formatmonth(year, month)
  print(month_calender)

  display_calendar()