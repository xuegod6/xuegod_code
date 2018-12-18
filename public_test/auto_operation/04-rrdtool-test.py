# -*- coding: utf-8 -*-
# @Time : 2018/12/12 17:35 
# @Author : for 
# @File : 04-rrdtool-test.py 
# @Software: PyCha
def f(x,I =[]):
    for i in range(x):
        I.append(i*i)
    print(I)
f(2)
f(3,[3,2,1])
f(3)
