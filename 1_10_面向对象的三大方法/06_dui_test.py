# -*- coding: utf-8 -*-
# @Time : 2019/1/19 22:04 
# @Author : for 
# @File : 06_dui_test.py 
# @Software: PyCharm
class Base(object):
    def test(self):
        print('base')
class A(Base):
    def test1(self):
        print('test1')
class B(Base):
    def test2(self):
        print('test2')
class C(B,A):
    pass
c = C()
c.test()
c.test1()
c.test2()
print(c.__class__.__mro__)
#
# class Base:
#     def __init__(self):
#         print('base')
#     def test(self):
#         print('base_test')
# class A(Base):
#     def __init__(self):
#         print('A')
# class B(Base):
#     def __init__(self):
#         print('B')
#     def test(self):
#         print('b_test')
# class C(A,B):
#     pass
# c =C()
# c.test()
# #访问顺序
# print(c.__class__.__mro__)














