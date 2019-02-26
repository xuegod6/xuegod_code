# -*- coding: utf-8 -*-
# @Time : 2019/1/14 21:29 
# @Author : for 
# @File : 03_yield_test.py 
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
# it = iter(gen)
# print(next(it))
# print(next(it))
# print(next(it))
# print(gen)
# for i in gen:
#     print(i)
# print(list(gen))
gen = (x**2 for x in range(1,5))#元组不可修改
print(gen)
it= iter(gen)
print(next(it))
for i in gen:
    print(i)














