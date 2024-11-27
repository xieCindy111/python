import os
import time
import copy
import keyboard
import random
#定义棋盘
def qipan(l2):
    l0=[]
    for i in range(20):
        l0.append([])
        for j in range(20):
            if i==0 or i==19 or j==0 or j==19:
                l0[i].append('#')
            elif [i+1,j+1] in l2:
                l0[i].append('*')
            elif [x0,y0]==[i+1,j+1]:
                l0[i].append('$')
            else:
                l0[i].append(' ')
    return l0
def start(l):
    for i in range(20):
        for j in range(20):
            if j==19:
                print(l[i][j],end='\n')
            else:
                print(l[i][j],end=' ')
#定义初始蛇位置
l2=[[2,6],[2,5],[2,4],[2,3],[2,2]]
#定义屏幕刷新
def f(l):
    os.system('cls' if os.name=='nt' else 'clear')
    print(start(qipan(l)))
    print('score:%d body:%d' % (score,body))
    
#定义食物位置
x0=random.randint(2,19)
y0=random.randint(2,19)
j=1
a=1
#开始游戏
p=input('start or not:')
#选择蛇的行进速度
speed=input('choose your speed(low/medium/fast):')
if speed=='low':
    x=0.3
elif speed=='medium':
    x=0.2
elif speed=='fast':
    x=0.1
score=0
body=5
while p=='start':
    m=copy.deepcopy(l2)
    if keyboard.is_pressed('w'):
        j=0
        a=0
    elif keyboard.is_pressed('a'):
        j=1
        a=0
    elif keyboard.is_pressed('s'):
        j=0
        a=1
    elif keyboard.is_pressed('d'):
        j=1
        a=1
    if a==0:
        l2[0][j]-=1
        for i in range(1,len(m)):
            l2[i]=m[i-1]
        if [x0,y0] in l2:
            score+=1
            body+=1
            l2.append(m[-1])
            x0=random.randint(2,19)
            y0=random.randint(2,19)
    else:
        l2[0][j]+=1
        for i in range(1,len(m)):
            l2[i]=m[i-1]
        if [x0,y0] in l2:
            score+=1
            body+=1
            l2.append(m[-1])
            x0=random.randint(2,19)
            y0=random.randint(2,19)
    if l2[0][0]==1 or l2[0][1]==1 or l2[0][0]==20 or l2[0][1]==20:
        p='end'
    if l2[0] in m:
        p='ending'
    if p=='start':
        f(l2) 
        time.sleep(x)
    while p=='end':
        f(m)
        print('you hit the boundary')
        time.sleep(1)
    while p=='ending':
        f(m)
        print('you hit the body')
        time.sleep(1)

