# -*- coding: utf-8 -*-
# @Time : 2019/1/19 22:15 
# @Author : for 
# @File : 07_chongxie_test.py 
# @Software: PyCharm
# class Dog(object):
#     def print_self(self):
#         print('Hello,I am dog')
# class Tom(Dog):
#     def print_self(self):
#         #调用父类的方法
#         # super().print_self()
#         # Dog.print_self(self)
#         print('Hi I am tom')
#
# T = Tom()
# T.print_self()

# class Dog(object):
#     def __init__(self,name):
#         self.name = name
#         self.color = '黄色'
#
# # class Tom(Dog):
#     def __init__(self,name):
#         # super(Tom,self).__init__(name)
#         # Dog.__init__(self,name)
#         super().__init__(name)
#     def getNaem(self):
#         print(self.name)
# T = Tom('Lucky')
# T.getNaem()
# try:
#     pass
# except NameError:
#     pass
#
#
#
# class Dog(object):
#     def print_self(self):
#         print('Hello,I am dog')
# class Tom(Dog):
#     def print_self(self):
#         #调用父类的方法
#         # super().print_self()
#         # Dog.print_self(self)
#         print('Hi I am tom')
# def func(object):
#     object.print_self()
# tom = Tom()
# func(tom)
#
# dog = Dog()
# func(dog)
#



class Base:
    def __init__(self):
        print('base')
    def test(self):
        print('base_test')
class A(Base):
    def __init__(self):
        print('A')
class B(Base):
    def __init__(self):
        print('B')
    def test(self):
        print('b_test')
class C(A,B):
    pass
c =C()
c.test()
#访问顺序
print(c.__class__.__mro__)



