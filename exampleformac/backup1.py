#!/usr/bin/python3
#Filename:backup1.py
#基础版本备份
import os
import time
#指定需要备份的文件
list=['/Users/xiexinyu/Desktop/exampleforwin','/Users/xiexinyu/Desktop/pythonformac']
#指定备份目标目录
target_dir='/Users/xiexinyu/Desktop/backup'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr '%s' %s" % (target,' '.join(list))
if os.system(zip_command)==0:
    print('successful back up to',target)
else:
    print('failed')
