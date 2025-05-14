import sys, datetime

#Python Version Checker. We need to import sys before a printing python version
print(sys.version)


#3. Python: Print current time and date, Convertion of time.
current_time_now = datetime.datetime.now()
print(current_time_now)

# Print the current date and time in a specific format
print(current_time_now.strftime("%Y-%m-%d %H:%M:%S"))

# current time in 12-hour format with AM/PM notation
now = datetime.datetime.now()
current_time_now = now.strftime("%I:%M %p")
print("Current time:", current_time_now)


now = datetime.datetime.now()
formatted_date_time = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted_date_time)


today = datetime.datetime.now()
future_date = today + datetime.timedelta(days=1000)

print(future_date)