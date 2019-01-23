# -*- coding: utf-8 -*-
# @Time : 2019/1/22 20:47 
# @Author : for 
# @File : 02_new_test.py 
# @Software: PyCharm
# class A(object):
#     def __init__(self):
#         print('这是init方法')
#     def __new__(cls, *args, **kwargs):
#         print('这是new方法')
#         return object.__new__(cls)
# A()

class A(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #加入我们要生产的参数
    def __new__(cls,name,age):
        print(cls)
        ret = object.__new__(cls)
        return ret
a = A('for',18)
print(a.name)