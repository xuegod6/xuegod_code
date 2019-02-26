# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 15:28
# @Author  : for 
# @File    : 02_dec_test.py
# @Software: PyCharm
def Dec(func):
    def inner():
        func()
        print('I come from china')
    return inner
@Dec#func1 = Dec(func1)
def func1():
    print('this is xuegod1')
#dec的调用，func1这是一个函数，返回inner 赋值f1
func1()