# -*- coding: utf-8 -*-
# @Time : 2019/1/5 10:34 
# @Author : for 
# @File : 07_yiele_test.py 
# @Software: PyCharm
# def myyiled():
#     print('即将生成2')
#     yield 2
#     print('即将生成3')
#     yield 3
#     print('即将生成5')
#     yield 5
#     print('即将生成7')
#     yield 7
#     print('生成结束')
# gen = myyiled()
# # print(gen)
# # for i in gen:
# #     print(i)
# it = iter(gen)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# # print(next(it))
# gen = (x**2 for x in range(1,5))
#
# it = iter(gen)
# print(next(it))
# print(next(it))
# print(next(it))

# print(gen)
# for i in gen:
#     print(i)
# list1 = [i for i in range(10)]
# print(list1)
# list1 = []
# for i in range(10):
#     list1.append(i)
# print(list1)



# for x,y in my(numbers,names):
#     print(y,'的客服电话是:',x)
# x,y = (1,2)
# print(x)
# print(y)
names = ['中国移动','中国电信','中国联通']
numbers = [10086,10000,10010,9558]
def myzip(iter1,iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    while True:
        a = next(it1)
        b = next(it2)
        yield (a,b)
for t in myzip(numbers,names):
    print(t)



# for t in enumerate(names,1):
#     print(t)
# def myenum(iterable):
#     it = iter(iterable)
#     i = 0
#     while True:
#         a = next(it)
#         yield (i,a)
#         i += 1
# for i in myenum(names):
#     print(i)
