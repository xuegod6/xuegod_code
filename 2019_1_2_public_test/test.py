# -*- coding: utf-8 -*-
# @Time : 2019/1/2 12:38 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
def Out(info):
    def Dec(func):
        def inner(name):
            print('info is %s'%info)
            func(name)
            print('come from china')
        return inner
    return Dec
#直接调用 返回 Dec
@Out('装饰器传递参数')
# func1 = Out('装饰器传参')(func1)
def func1(name):
    print('this is xuegod1')
    print('I am %s'%name)

func1('for')