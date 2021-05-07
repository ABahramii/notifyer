# This script send desktop notification to remind you a repetitive work

import os
import time

from time_utils import *

print("Note: Enter times in format 00:00:00", end = "\n\n")

total = input("Enter total time: ")
per = input("Enter alternation time: ")

#convert times to seconds
total_seconds = hr_to_sec(total[0:2]) + min_to_sec(total[3:5]) + int(total[6:8])

per_seconds = hr_to_sec(per[0:2]) + min_to_sec(per[3:5]) + int(per[6:8])

# calculate number of repeats
num = int(total_seconds / per_seconds)

num += 1
for i in range(1, num):
    time.sleep(per_seconds)
    os.system("notify-send \"Hello Programmer!\" \"Let's move your body :)\"")  # run command
