# -*- coding: utf-8 -*-
# @Time : 2019/1/11 21:56 
# @Author : for 
# @File : 06_dec_test.py 
# @Software: PyCharm
# def outer(func):
#     def inner(name): #name == for
#         func(name)#func1()
#         print('inner 中的%s'%name)
#     return inner
# @outer# func1 = outer(func1)
# def func1(name):
#     print('this is xuegod1')
#     print('I am %s'%name)
# func1('for')
def outer(func):
    def inner(*args,**kwargs):
        c = func(*args,**kwargs)
        print(c)
    return inner
@outer
def func1(a,b=1):
    return a * b
func1(5,5)