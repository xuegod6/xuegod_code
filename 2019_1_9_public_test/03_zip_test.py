# -*- coding: utf-8 -*-
# @Time : 2019/1/9 15:20 
# @Author : for 
# @File : 03_zip_test.py 
# @Software: PyCharm
# numbers = [10086, 10000, 10010, 9558]
#
# names = ['中国移动', '中国电信', '中国联通']
#
#
# def myzip(iter1,iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     while True:
#         a = next(it1)
#         b = next(it2)
#         yield (a,b)
# for t in myzip(numbers,names):
#     print(t)


# for x,y in zip(numbers,names):
#     print(y,'的客服电话是:',x)
# # (10086,中国移动)
# a,b = (10,20)
# print(a)


names = ['中国移动', '中国电信', '中国联通']
# for t in enumerate(names,1):
#     print(t)

def muenum(iterable,start):
    it = iter(iterable)
    i = start
    while True:
        a = next(it)
        yield (i,a)
        i += 1
a = muenum(names,1)
print(list(a))






