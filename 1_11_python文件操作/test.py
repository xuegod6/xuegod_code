# -*- coding: utf-8 -*-
# @Time : 2019/1/22 9:59 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
# class People:
#     def __init__(self,name):
#         print('__init__被调用了')
#         self.name = name
#     def __del__(self):
#         print('__del__正在被调用了')
#         print('正在删除……%s'%self.name)
# p = People('for')
# # print(p.name)
# print(p.name)

#
# class Singleton(object):
#     __instance = None
#     def __new__(cls,*args,**kwargs):
#         #如果__instance没有赋值则一直为none
#         #接下来我们利用new方法，创造出一个对象，并且更改__instance的值
#         #保证私有属性__instance不为空！然后经过逻辑判断只为
#         if not cls.__instance:#判断是否__instance为空，为空就生成
#             cls.__instance = object.__new__(cls)
#         #__instance不为空，直接返回
#         return cls.__instance
# #第一个实例对象
# a = Singleton('for',18)
# #第二个实例对象
# b = Singleton('bin',8)
# print(id(a))
# print(id(b))

# class SingLeton(object):
#     __instance = None
#     __first_init = False
#     def __new__(cls,*args,**kwargs):
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#     def __init__(self,name,age):
#         if not self.__first_init:
#             self.name = name
#             self.age = age
#             #更改属性的私有类属性，并把它设置为True，下个对象调用时就不会执行这个if判断中的语句。
#             SingLeton.__first_init = True
# a = SingLeton('for',18)
# b = SingLeton('django',10)
# print(id(a))
# print(id(b))
# print(b.age)

#
# class Hero:
#     def __del__(self):
#         print("英雄已阵亡")
# #创建一个实例
# man1 = Hero()
# #指向这个实例的引用计数为2
# man2 = man1
# #删除引用计数
# del man1
#
# print('程序结束')
#coding = utf-8
# class A(object):
#     def __init__(self):
#         print('这是init方法')
#     def __new__(cls, *args, **kwargs):
#         print('这是new方法')
#         return object.__new__(cls)
# A()

# class A(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     #加入我们要生产的参数
#     def __new__(cls,name,age):
#         print(cls)
#         ret = object.__new__(cls)
#         return ret
# a = A('for',18)
# print(a.name)
# print()

# class Test(object):
#     def __init__(self,world):
#         self.world = world
#     def __str__(self):
#         print('__str__')
#         return 'world is %s'%self.world
# t = Test('for')
# # print(str(t))
# print(t)
