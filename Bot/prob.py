import datetime


class GetTime:
    time_now = str(datetime.datetime.now())
    year = time_now[0:4]
    day = time_now[8:10]
    month = time_now[5:7]
    hour = time_now[11:13]
    minutes = time_now[14:16]
    sec = time_now[17:19]


year = GetTime.year
day = GetTime.day
month = GetTime.month
hour = GetTime.hour
minutes = GetTime.minutes
sec = GetTime.sec

print(year, day, sec)

