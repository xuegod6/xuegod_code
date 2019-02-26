# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 14:57
# @Author  : for 
# @File    : 01_bibao_test.py
# @Software: PyCharm
# def outer():
#     #内嵌函数
#     def inner():
#         print('你歪的很')
#         #返回inner这个函数
#     return inner
# #返回inner 赋值给a这个变量，a==inner
# a = outer()
# # print(a)
# a()# a 的调用相当于 inner的调用




def outer(num):
    def inner(num_in):
        print('inner num_in is %d'%num_in)
        return num + num_in
    return inner
a = outer(20)
print(a(200))










