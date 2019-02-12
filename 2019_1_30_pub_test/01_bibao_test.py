# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 15:36
# @Author  : for 
# @File    : 01_bibao_test.py
# @Software: PyCharm
# def outer():
#     def inner():
#         print('大家新年快乐')
#     return inner
# a = outer()
# a()
def outer(num):
    def inner(num_in):
        print('inner num_in is %d'%num_in)
        return num + num_in
    return inner
a = outer(20)
print(a)
print(a(200))





