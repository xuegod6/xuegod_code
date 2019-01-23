# -*- coding: utf-8 -*-
# @Time : 2019/1/22 21:02 
# @Author : for 
# @File : 04_Singleton _test.py 
# @Software: PyCharm
# class Singleton(object):
# # #     __instance = None
# # #     def __new__(cls,name,age):
# # #         print(cls.__instance)
# # #         if not cls.__instance:
# # #             cls.__instance = object.__new__(cls)
# # #         return cls.__instance
# # # a = Singleton('for',18)
# # # b = Singleton('bai',8)
# # # print(id(a))
# # # print(id(b))
# # # a.age = 19
# # # print(b.age)


class SIngLeton(object):
    __instance = None
    __first_init = False
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,name,age):
        if not self.__first_init:
            self.name = name
            self.age = age
            SIngLeton.__first_init = True
a = SIngLeton('for',18)
b = SIngLeton('django',10)

# print(id(a))
# print(id(b))
# print(b.age)

















