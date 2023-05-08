import time

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
MONTH = DAY * 30
YEAR = MONTH * 12

def time_test(time_to_remind):
    year = (int(time_to_remind[0:4]) - 1970) * YEAR
    month = int(time_to_remind[5:7]) * MONTH
    day = int(time_to_remind[8:10]) * DAY
    hour = int(time_to_remind[11:13]) * HOUR
    print(hour)
    minute = int(time_to_remind[14:16]) * MINUTE
    time_now = time.strftime("%Y-%m-%d-%H.%M", time.localtime())
    print(time_now)
    print(time_to_remind)
    year_now = (int(time_now[0:4]) - 1970) * YEAR
    month_now = int(time_now[5:7]) * MONTH
    day_now = int(time_now[8:10]) * DAY
    hour_now = int(time_now[11:13]) * HOUR
    print(hour_now)
    minute_now = int(time_now[14:16]) * MINUTE
    reminder=(year+month+day+hour+minute) - (year_now+month_now+day_now+hour_now+minute_now)
    print(reminder)
    #time.sleep(reminder)
time_test('2023-05-09-00-05')