#!/usr/bin/python3
#Filename:backup2.py
#2.0版本备份,时间作为文件名，日期作为目录名
import os
import time
#指定需要备份的文件
list=['/Users/xiexinyu/Desktop/exampleforwin','/Users/xiexinyu/Desktop/pythonformac']
#指定备份目标目录
target_dir='/Users/xiexinyu/Desktop/'
mulu=target_dir+'backup'+time.strftime('%Y%m%d')
wenjian=time.strftime('%H%M%S')
if not os.path.exists(mulu):
    os.mkdir(mulu)
    print('secessful make mulu:',mulu)
target=mulu+os.sep+wenjian+'.zip'
zip_command="zip -qr '%s' %s" % (target,' '.join(list))
if os.system(zip_command)==0:
    print('successful back up to',target)
else:
    print('failed')
