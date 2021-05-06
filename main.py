# This script send desktop notification each 20 minutes to remind you a repetitive work

import os
import time

for i in range(1, 6):
    time.sleep(60 * 20) #second
    os.system("notify-send \"Hello Programmer!\" \"Let's move your body :)\"") #run command


