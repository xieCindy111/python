#!/usr/bin/python3
#Filename:classformac.py
class schoolmember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def tell(self):
        print('name:%s age:%d' % (self.name,self.age))
class teacher(schoolmember):
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary = salary
    def tell(self):
        print('name:%s age:%d salary:%d' % (self.name,self.age,self.salary))
class student(schoolmember):
    def __init__(self,name,age,score):
        schoolmember.__init__(self,name,age)
        self.score = score
    def tell(self):
        print('name:%s age:%d score:%d' % (self.name,self.age,self.score))
a = input('Are you a student or a teacher:')
if a=='student':
    x = input('Your name:')
    y = int(input('your age:'))
    z = int(input('your score:'))
    b = student(x,y,z)
    print(b.tell())
elif a=='teacher':
    x = input('Your name:')
    y = int(input('your age:'))
    z = int(input('your salary:'))
    b = teacher(x,y,z)
    print(b.tell())


            
    
