# -*- coding: utf-8 -*-
# @Time : 2019/1/19 21:20 
# @Author : for 
# @File : 04_pri_test.py 
# @Software: PyCharm
# class Parent:
#     __age = 10
#     def hello(self):
#         print(Parent.__age)
#
# p = Parent()
# p.hello()
# print(Parent.__age)


class Parent:
    def __init__(self,name,age):
        #私有实例属性
        self.__name = name
        self.age = age
    @property
    def hello(self):
        #内部访问
        print(self.__name)
        print(self.age)
p = Parent('xuegod',18)
print(p.hello)
print(p.age)#可以
# print(p.__name)#出错




# class Parent:
#     def __init__(self,name,age):
#         #私有实例属性
#         self.__name = name
#         self.age = age
#     def __func(self):
#         print('我是私有的实例方法')
#     def hello(self):
#         self.__func()
# p = Parent('xuegod',18)
# p.hello()
# # p.__func()