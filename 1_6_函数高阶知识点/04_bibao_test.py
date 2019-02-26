# -*- coding: utf-8 -*-
# @Time : 2019/1/11 21:22 
# @Author : for 
# @File : 04_bibao_test.py 
# @Software: PyCharm
# 1. 闭包函数必须有内嵌函数；
# 2. 内嵌函数需要引用该嵌套函数上一级namespace中的变量；
# 3. 闭包函数必须返回内嵌函数；

# def outer():
#     def inner():
#         print('我是inner')
#     return inner
#     # inner()
# # outer()()
# a = outer()
# print(a)
# a()# inner()

def outer(num):
    def inner(num_in):
        print('inner num_in is %d'%num_in)
        return  num + num_in
    return inner
a = outer(20)# a == inner
print(a(200)) #相当于inner（200）  之后打印









