# -*- coding: utf-8 -*-
# @Time : 2018/12/24 14:34 
# @Author : for 
# @File : 01_bibao_test.py 
# @Software: PyCharm
# def outer(num):
#     def inner(num_in):
#         print('inner num_in is %d'%num_in)
#         return num_in+num
#     return inner
#
# a = outer(20)
# # print(a)
# print(a(200))
#全局变量
x = 2
def outer():
    #嵌套变量
    x = 0
    def inner():
        #本地变量
        # x = 1
        global x
        x = x+1
        print(x)
    return inner
outer()()
print(x)















