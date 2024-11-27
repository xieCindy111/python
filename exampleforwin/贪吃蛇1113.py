import random
import time
#初始界面
def l0(m,x0,y0):
    l=[]
    for i in range(10):
        l.append([])
        for j in range(10):
            l[i].append(' ')
    for i in range(len(m)):
        a=m[i][0]
        b=m[i][1]
        l[a-1][b-1]='*'
    l[x0-1][y0-1]='#'
    return l
def start(l):
    for i in range(10):
        for j in range(10):
            if j !=9:
                print(l[i][j],end=' ')
            else:
                print(l[i][j],end='\n')
#用户点击
def move1(a0,x,y):
    if a0=='w':
        x-=1
    elif a0=='a':
        y-=1
    elif a0=='s':
        x+=1
    elif a0=='d':
        y+=1
    else:
        print('you hit a wrong button')
    return [x,y]
def local0(m,move):
    n=m[:]
    m[0]=move
    if move!=[x0,y0]:
        for i in range(1,len(n)):
            m[i]=n[i-1]
    else:
        for i in range(1,len(n)):
            m[i]=n[i-1]
        m.append(n[-1])
    return m
#游戏开始
p=input('start or not:')
while p=='start':
#定义贪吃蛇初始位置
    x1=1
    y1=1
    m=[[x1,y1]]
#定义食物位置
    x0=random.randint(1,10)
    y0=random.randint(1,10)
    l=l0(m,x0,y0)
    start(l)
    you='start'
    while you=='start':
        if len(m)==5:
            print('you win')
            you='end'
        else:
            x=m[0][0]
            y=m[0][1]
            a0=input('choose your move(w/a/s/d):')
            move=move1(a0,x,y)
            if move in m:
                print('you hit the body')
                you='end'
            else:
                m=local0(m,move)
                if move==[x0,y0]:
                    x0=random.randint(1,10)
                    y0=random.randint(1,10)
                if move[0]==0 or move[1]==0:
                    print('you hit a boundary')
                    you='end'
                else:
                    l=l0(m,x0,y0)
                    start(l)
#游戏结束暂停3秒后询问是否继续下一轮
    time.sleep(3)
    p=input('start or not:')
