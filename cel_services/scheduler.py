import time, subprocess
from database import ScheduledEvent
from datetime import datetime

# https://stackoverflow.com/questions/1359383/run-a-process-and-kill-it-if-it-doesnt-end-within-one-hour
'''
1. query for tasks occuring during this interval
2. spawn subprocesses for each event
'''
dayNum = {
  0:"Mon",
  1:"Tues",
  2:"Wed",
  3:"Thurs",
  4:"Fri",
  5:"Sat",
  6:"Sun"
}

def get_repeats(now):
    dayName = dayNum[now.weekday()]
    return ScheduledEvent.select().where(
        ScheduledEvent.repeat.contains(dayName),
        ScheduledEvent.hour === now.hour)

def poll():
    now = datetime.now()
    # get the recurring events for today
    dailies = get_repeats(now)
