from django.core.mail import send_mail
from celery import shared_task
import time

MINUTE = 60
HOUR = MINUTE * 60
DAY = HOUR * 24
MONTH = DAY * 30
YEAR = MONTH * 12
@shared_task
def send_email_task(message_mail, time_to_remind, to_mail):
    year = (int(time_to_remind[0:4]) - 1970) * YEAR
    month = int(time_to_remind[5:7]) * MONTH
    day = int(time_to_remind[8:10]) * DAY
    hour = int(time_to_remind[11:13]) * HOUR
    minute = int(time_to_remind[14:16]) * MINUTE
    time_now = time.strftime("%Y-%m-%d-%H.%M", time.localtime())
    year_now = (int(time_now[0:4]) - 1970) * YEAR
    month_now = int(time_now[5:7]) * MONTH
    day_now = int(time_now[8:10]) * DAY
    hour_now = int(time_now[11:13]) * HOUR
    minute_now = int(time_now[14:16]) * MINUTE
    reminder=(year+month+day+hour+minute) - (year_now+month_now+day_now+hour_now+minute_now)
    if reminder < 0:
        return 'reminder cant be in past'
    elif reminder > DAY * 2:
        return 'reminder cant be more than 2 days'
    else:
        time.sleep(reminder)
        send_mail(message_mail,
                time_to_remind, 
                '123rrtyis2@gmail.com', 
                [to_mail], 
                fail_silently=False, 
                auth_user='123rrtyis2@gmail.com', 
                auth_password='hwtmamsvabdnbmue')
    return time_to_remind , time_now , reminder
