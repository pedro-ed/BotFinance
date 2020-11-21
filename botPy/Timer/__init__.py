import time
import datetime
def SleepMoment(segund):
    sleep = True
    while sleep:
        time.sleep(1.0)
        sleep = False if datetime.datetime.now().second == segund else True
