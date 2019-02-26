# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 15:06
# @Author  : for 
# @File    : 02_dec_test.py
# @Software: PyCharm
# def func1():
#     print('this is xuegod1')
# def outer(func):
#     def inner():
#         func()
#         print('I come from china')
#     return inner
# func1 = outer(func1)
# print(func1)
# def a(info):
#     def outer(func):
#         def inner():
#             func()
#             print('I come from china')
#         return inner
#     return  outer
# @a('传参')## func1 = outer(func1)
# def func1():
#     print('this is xueogd1')
# func1()





def outer(func):
    def inner(name):
        func(name)
        print('inner中的 %s'%name)
    return inner
@outer#func1 = outer(func1)
def func1(name):
    print('this is xuegod1')
    print('I am %s'%name)
func1('for')
