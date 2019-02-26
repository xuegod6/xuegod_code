# -*- coding: utf-8 -*-
# @Time : 2019/1/9 15:03 
# @Author : for 
# @File : 02_yield_test.py 
# @Software: PyCharm
# def myyield():
#     print('即将生成2')
#     yield 2
#     print('即将生成3')
#     yield 3
#     print('即将生成5')
#     yield 5
#     print('即将生成7')
#     yield 7
#     print('生成结束')
# gen = myyield()
# print(gen)
# it = iter(gen)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for i in gen:
#     print(i)

gen = (x**2 for x in range(1,5))
# print(list(gen))
# for i in gen:
#     print(i)
i = iter(gen)
print(next(i))











