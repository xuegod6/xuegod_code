# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 16:00
# @Author  : for 
# @File    : 02_dec_test.py
# @Software: PyCharm
def outer(func):
    def inner(name):
        #name = 'for'
        func(name)#func1('for')
        print('inner 中的 %s'%name)
    return inner
@outer
#等同于func1 = outer(func1)
#第一个func1 是为了接受返回的函数inner
#第二个func1 是作为一个实参传递给形参func
def func1(name):
    print('this is xuegod1')
    print('I am %s '%name)
    # print('I come from china')
func1('for')# inner()