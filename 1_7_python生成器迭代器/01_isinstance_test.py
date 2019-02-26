# -*- coding: utf-8 -*-
# @Time : 2019/1/14 20:46 
# @Author : for 
# @File : 01_isinstance_test.py 
# @Software: PyCharm
from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance({1,2,3},Iterable))
print(isinstance({'a':1},Iterable))
print(isinstance(range(1),Iterable))