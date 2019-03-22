# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 20:41
# @Author  : for 
# @File    : 01_isinstance_test.py
# @Software: PyCharm
from collections import Iterable


print(isinstance('abc',Iterable))# str
print(isinstance([1,2,3],Iterable))#list
print(isinstance((1,2,3),Iterable))#tuple
print(isinstance({1,2,3},Iterable))#set
print(isinstance({'a':1},Iterable))#dict
print(isinstance(1,Iterable))#int