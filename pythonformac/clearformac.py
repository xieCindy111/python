#!/usr/bin/python3
#Filename:clear
import time
import os
import sys
while True:
#刷新屏幕，清除屏幕内容
    os.system('clear')
    sys.stdout.flush()
    print('a')
    time.sleep(1)
