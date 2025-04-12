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
        ScheduledEvent.hour === now.hour).execute()

# the instructions don't give a specific scheduled task
# so this is just meta code
def perform_task(event):
    # spawn a task
    # using the popen keep track of the task
    # using the instructions from stackoverflow use the duration
    # to ensure the subprocess doesn't stick around for to long
    # if the process succeeds mark last_run as now and save
    pass

def poll():
    now = datetime.now()
    # get the recurring events for today
    dailies = get_repeats(now)
    map(perform_task, dailies)
