from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
print(day,month,year,hour,minute)
timestamp =now.timestamp()
print(timestamp)
timenow = now.strftime("%m/%d/%Y, %H:%M:%S")
print(timenow)

from datetime import date
today = '5 December, 2019'
date_object = datetime.strptime(today,'%d %B, %Y')
print(date_object)
now = datetime.now()
new_year = datetime(2025,1,1)
diff = new_year-now
print(diff)
old = datetime(1970,1,1)
diff = now - old
print(diff)
print(timestamp)