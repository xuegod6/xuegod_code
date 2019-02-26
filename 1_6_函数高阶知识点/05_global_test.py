# -*- coding: utf-8 -*-
# @Time : 2019/1/11 21:44 
# @Author : for 
# @File : 05_global_test.py 
# @Software: PyCharm
# x = 2
# def outer():
#     x = 0
#     def inner():
#         # global x
#         x = 1
#         print(x)
#     print(x)
#     return inner
# outer()()
# print(x)
x = 10
def outer():
    x = 2
    def inner():
        nonlocal x
        # x = 0
        x = x+1
        print(x)
    inner()
    print(x)
outer()







