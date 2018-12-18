# -*- coding: utf-8 -*-
# @Time : 2018/12/11 14:34 
# @Author : for 
# @File : 07-bibao_test.py 
# @Software: PyCharm
# def outer(num):
# #
# #     def inner(num_in):
# #
# #         print('inner_num_in is %d'%num_in)
# #
# #         return num+num_in
# #
# #     return inner
# #
# # a = outer(20)
# # # outer(20) == inner
# # # a = inner
# # # a(200)
# # print(a(200))

x = 2
def outer():
    global x
    x = 0
    def inner():
        global x
        print(x)
    return inner
# outer()() # inner()
a = outer()
a()
print(x)















