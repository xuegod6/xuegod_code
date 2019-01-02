# -*- coding: utf-8 -*-
# @Time : 2019/1/2 14:56 
# @Author : for 
# @File : 03_func_test.py 
# @Software: PyCharm

def outer(func):
    def inner():
        func()
        print('I come from china')
    return inner
@outer# func1 = outer(func1)
def func1():
    print('this is xueogd1')
@outer
def func2():
    print('this is xuegod2')
# print(func1)
func1()
func2()