# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 22:00
# @Author  : for 
# @File    : 04_function_test.py
# @Software: PyCharm
#for 很帅
# def for_test(a):
#     "for 很帅"
#     # print('for 很帅')
#     return a+1
# a = for_test(10)
# print(a)

# 位置参数
# def func(name,city='beijing'):
#     print('I am %s,I am from %s'%(name,city))
# func('for')
# func('xuegod','for')

def say_hello(e,f,p =2,*args,**kwargs):
    a =1
    b =2
    print(a,b)
say_hello(1,2,3,4,5,a=1)


