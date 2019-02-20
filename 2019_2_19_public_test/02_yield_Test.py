# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 10:34
# @Author  : for 
# @File    : 02_yield_Test.py
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
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# for i in gen:
#     print(i)

gen = (x **2 for x in range(1,5))
print(gen)
# for i in gen:
#     print(i)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))









