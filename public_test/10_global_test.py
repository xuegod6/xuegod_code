# -*- coding: utf-8 -*-
# @Time : 2018/12/12 10:05 
# @Author : for 
# @File : 10_global_test.py 
# @Software: PyCharm
x = 2
def outer():
    x = 0
    def inner():
        global x
        x = x+1
        print(x)
    return inner
outer()()#inner()
print(x)