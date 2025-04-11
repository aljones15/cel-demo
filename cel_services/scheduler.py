import psutil, time, subprocess

# https://stackoverflow.com/questions/1359383/run-a-process-and-kill-it-if-it-doesnt-end-within-one-hour
'''
1. query for tasks occuring during this interval
2. spawn subprocesses for each event
'''
def poll():
    print("poll")
