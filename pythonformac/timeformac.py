from time import *
#time（）获取当前时间戳（从1970-01-01 00:00：00到现在的秒数）
#localtime（）当地时间（元组形式）默认从当前时间戳开始，可以指定参数作为时间戳
#gmtime（）获取当前时间的struct_time形式
#ctime（）获取字符串形式的时间，参数是时间戳
#asctime（）获取字符串形式的时间，参数是时间元组
#mktime（）时间元组转换为时间戳
#strftime（）时间元组格式化为时间字符串，默认输入localtime（）
#strpime（）时间字符串转化为时间元组，默认输入localtime（）
#sleep（）暂停
#perf_counter（）返回时间计数值，单位秒，但是起点不确定，需要调用差值
a=ctime(time())
b=asctime(localtime(time()))
c=asctime(gmtime(time()))
print(a)
print(b)
print(c)
print(localtime())
start=perf_counter()
sleep(5)
end=perf_counter()
print(end-start)
print(time())
