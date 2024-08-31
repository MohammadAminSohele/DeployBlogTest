from .import jalali

from django.utils import timezone

def JalaliConverter(time):
    # return "hello"
    jmonth=['فروردین','اردیبهشت','خرداد','تیر','مرداد','shahrivar','مهر','آبان','آذر','دی','بهمن','اسفند']
    time=timezone.localtime(time)
    time_to_str="{},{},{}".format(time.year,time.month,time.day)
    time_to_tuple=jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list=list(time_to_tuple)
    for index,month in enumerate(jmonth):
        if time_to_list[1]==index+1:
            time_to_list[1]=month
            break
    output="Date:{}/{}/{} clock:{}:{}".format(
        time_to_list[0],
        time_to_list[1],
        time_to_list[2],
        time.hour,
        time.minute
    )
    return output