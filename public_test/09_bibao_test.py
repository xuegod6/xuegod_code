# -*- coding: utf-8 -*-
# @Time : 2018/12/12 9:56 
# @Author : for 
# @File : 09_bibao_test.py 
# @Software: PyCharm
def outer(num):

    def inner(num_in):

        print('inner,num_in is %d'%num_in)
        return num+num_in

    return inner
# a == inner
a = outer(20) # inner
# print(a)
#a(200)==inner(200)
print(a(200))