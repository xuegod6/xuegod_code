# -*- coding: utf-8 -*-
# @Time : 2018/12/24 15:02 
# @Author : for 
# @File : 02_dec_test.py 
# @Software: PyCharm
def outer(func):# func = = func1
    def inner():
        func()# func1()
        print(' I come form china')
    return inner

@outer
#func1 = outer(func1)
def func1():
    print('this is xuegod1')
func1()
# f1 = outer(func1) # fi == inner
# f1()

# func2()