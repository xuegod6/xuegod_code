# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:29
# @Author  : for 
# @File    : 02_yield_test.py
# @Software: PyCharm
# def my_yield():
#     print('即将生成2')
#     yield 2
#     print('即将生成3')
#     yield 3
#     print('即将生成5')
#     yield 5
#     print('即将生成7')
#     yield 7
#     print('生成结束')
# gen = my_yield()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

gen = (x**2 for x in range(1,5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))















