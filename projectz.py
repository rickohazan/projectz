import pyautogui
import datetime
import time
from random import randrange

# Define the time intervals for pressing the button
time_intervals = [
    {'start_time': datetime.time(6, 0), 'end_time': datetime.time(23, 59), 'interval': randrange(17, 22)},
    {'start_time': datetime.time(2, 59), 'end_time': datetime.time(4, 0), 'interval': randrange(105, 130)},
    {'start_time': datetime.time(4, 0), 'end_time': datetime.time(6, 0), 'interval': randrange(25, 35)},
]
while True:
    current_time = datetime.datetime.now().time()
    for interval in time_intervals:
        if interval['start_time'] <= current_time <= interval['end_time']:
            time.sleep(20)
            pyautogui.hotkey('command', 'r')
            time.sleep(15)
            pyautogui.scroll(-3000)
            time.sleep(15)
            pyautogui.click(x=410, y=790)  #claim
            time.sleep(15)
            pyautogui.click(x=870, y=540)  # sign
            time.sleep(interval['interval'] * 60)  # Convert interval from minutes to seconds
