# -*- coding: utf-8 -*-
# @Time : 2019/1/2 13:06 
# @Author : for 
# @File : 01_two_dec_test.py 
# @Software: PyCharm
def set_fun1(func1):
    print("set_fun1")
    def call_fun1():
        print("call_fun1")
        func1()
    return call_fun1
def set_fun2(func2):
    print("set_fun2")
    def call_fun2():
        print("call_fun2")
        func2()

    return call_fun2


@set_fun2
@set_fun1
def test():
    print("test")
test()
