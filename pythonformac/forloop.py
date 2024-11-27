#！/usr/bin/python3
#Filename:forloop.py
#for循环
for i in range(5):
    print(i)
print('done')

#while循环
i=0
while True:
    print(i)
    i+=1
    if i==5:
#break直接结束循环
        break

i=0
while i<10:
    i+=1
    if i==5:
#continue跳过下一语句继续循环
        continue
    print(i)    
