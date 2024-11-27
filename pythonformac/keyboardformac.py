#!/usr/bin/python3
#Filename:keyboardformac
#文件名不要直接用库名否则无法执行
#用is_key_down操控松开按键时不再受影响
import keyboard
import time
is_key_down=False
i=0
while True:
    if keyboard.is_pressed('a'):
        print('按下a键')
        i=1
        if not is_key_down:
            is_key_down=True
    else:
        if is_key_down:
            print('已松开')
            is_key_down=False
            i=0
    time.sleep(0.1)
    print(i)

