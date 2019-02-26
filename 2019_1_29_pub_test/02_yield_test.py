# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 15:07
# @Author  : for 
# @File    : 02_yield_test.py
# @Software: PyCharm
# def myyield():
#     print('即将生成2')
#     yield 2
#     print('即将生成3')
#     yield 3
#     print('即将生成4')
#     yield 5
#     print('即将生成5')
#     yield 7
#     print('生成结束')
# gen = myyield()
# # print(gen)
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# it = iter(gen)
# print(it)

gen = (x ** 2 for x in range(1,5))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
for i in gen:
    print(i)





