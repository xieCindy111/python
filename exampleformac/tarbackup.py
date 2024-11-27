#!/usr/bin/python3
#Filename:tarbackup.py
#备份
import os
import time
#指定需要备份的文件
list1=['/Users/xiexinyu/Desktop/exampleforwin','/Users/xiexinyu/Desktop/pythonformac']
#指定备份目标目录
target_dir='/Users/xiexinyu/Desktop/'
mulu=target_dir+'backup'+time.strftime('%Y%m%d')
wenjian=time.strftime('%H%M%S')
#指定文件用途
comment=input('文件用途：')
if not os.path.exists(mulu):
    os.mkdir(mulu)
    print('secessful make mulu:',mulu)
#在压缩包名字后加上用途方便管理
if len(comment)==0:
    target=mulu+os.sep+wenjian+'.tar.gz'
else:
    target=mulu+os.sep+wenjian+'_'+\
    comment.replace(' ','_')+'.tar.gz'
tar="tar -cvzf '%s' %s" % (target,' '.join(list1))
if os.system(tar)==0:
    print('successful backup',target)
else:
    print('failed')
#-c表示创建一个归档
#-v表示交互
#-z表示使用gzip滤波器
#-f表示如有一个同名文件，将被替换
#-X表示不备份相应文件，如：*～表示以～结尾的所有文件
