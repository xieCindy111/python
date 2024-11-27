#！/usr/bin/python3
#Filename:sysmodule.py
import sys

#sys.argv（列表）\sys.path
#python sysmodule.py hello world
print('command line arguments:')
for i in sys.argv:
    print(i)
print('PATH:',sys.path)

#判断是否单独运行
if __name__=='__main__':
    print('yes')
else:
    print('no')

#输入module模块,在同一目录或在sys.path目录里
import module
module.min(1,2)
#列出模块标识符：函数、类、变量
print(dir(module))