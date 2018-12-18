# -*- coding: utf-8 -*-
# @Time : 2018/12/11 14:58 
# @Author : for 
# @File : 07_zhuanshi_test.py 
# @Software: PyCharm
def Dec(func):
    # print(func)
    def inner():
        func()
        print('i come form china')
    return inner
@Dec      #func1 = Dec(func1)
def func1():
    print('this is xuegod1')
func1()