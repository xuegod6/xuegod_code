# -*- coding: utf-8 -*-
# @Time : 2019/1/2 14:35 
# @Author : for 
# @File : 02_bibao_test.py 
# @Software: PyCharm
x = 2
def outer(num):
    x = 0
    def inner(num_in):
        global x
        x = x + 1
        print(x)
    return inner
a = outer(20) # inner ==a
a(200)
print(x)