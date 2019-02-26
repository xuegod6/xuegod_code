# -*- coding: utf-8 -*-
# @Time : 2019/1/14 22:25 
# @Author : for 
# @File : 05_enumerate_test.py 
# @Software: PyCharm
names = ['中国移动', '中国电信', '中国联通']
# for t in enumerate(names,1):
#     print(t)
def myenum(iterable,i=2):
    it = iter(iterable)
    while True:
        a = next(it)
        yield (i,a)
        i += 1
for t in myenum(names):
    print(t)