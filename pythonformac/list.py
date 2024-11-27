#创建列表
list1=[10086,'yidong',[1,2,3,4,5,6]]
#列表长
print(len(list1))
#从头开始输出列表
print(list1[0:])
#增加元素
list1.append('i\'m here')
#列表长和列表最后一位
print(len(list1))
print(list1[-1])
#删除某一元素
print(list1.pop(1))
print(len(list1))
print(list1)

list2=[[1,2,3],
       [4,5,6],
       [7,8,9]]
print(list2)
print(list2[1])
#列表的列
a=[x[1] for x in list2]
print(a)
b=[row[1] for row in list2 if row[1]%2==0]
print(b)
