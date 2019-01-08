# -*- coding: utf-8 -*-
# @Time : 2019/1/7 21:11 
# @Author : for 
# @File : 03_type_func_test.py 
# @Software: PyCharm
#位置传参

def func(name,city):
    print('I am %s,I am from %s'%(name,city))

func(name='for',city='xuegod')
func(city='xuegod',name='for')


关键字传参
def func(name,city):
    print('I am %s,I am from %s'%(name,city))

func(name='for',city='xuegod')
func(city='xuegod',name='for')


 默认在传参
def func(name,city='beijing'):
    print('I am %s,I am from %s'%(name,city))

func(name='for',city='xuegod')
func(city='xuegod',name='for')
func(name='for')
func(name='for',city='xuegod')
func('for','japan')



#错误演示
def func(city='beijing',name):
    print('I am %s,I am from %s'%(name,city))

#元祖参数在
def say_hello(*args):
    print(args)
say_hello()
say_hello(1)
say_hello(1,2,3,4,5)
say_hello()
#字典参数组
def say_hello(**kwargs):
    print(kwargs)
say_hello()
say_hello(a =1)
say_hello(a =1,b = 2,c = 3)
# say_hello()


def say_hello(e,f,p = 2,*args,**kwargs):
    a = args
    b  =kwargs
    print(a,b)
say_hello(1,2,3,a=1)



