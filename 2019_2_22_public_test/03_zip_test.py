# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:42
# @Author  : for 
# @File    : 03_zip_test.py
# @Software: PyCharm
numbers = [10086, 10000, 10010, 9558]


# for x,y in zip(numbers,names):
#     print(y,'客服电话是:',x)
# def my_zip(iter1,iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     while True:
#         a = next(it1)
#         b = next(it2)
#         yield (a,b)
# for t in my_zip(numbers,names):
#         print(t)

names = ['中国移动', '中国电信', '中国联通']
# for t in enumerate(names,1):
#     print(t)

def my_enum(iterable,i = 0):
    it = iter(iterable)
    i = i
    while True:
        a = next(it)
        yield (i,a)
        i += 1
for t in my_enum(names,1):
    print(t)









