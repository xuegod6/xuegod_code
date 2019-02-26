# -*- coding: utf-8 -*-
# @Time : 2018/12/28 11:30 
# @Author : for 
# @File : 05-重新创建数组_test.py 
# @Software: PyCharm
#numpy.asarry
import numpy as np

# x = [1,2,3]
# a = np.asanyarray(x)
# print(a)
# x = (1,2,3)
# a = np.asarray(x)
# print(a)

# x = [(1,2,3),(4,5)]
#
# a = np.asarray(x)
# print(a)

# x = [1,2,3]
# a = np.asarray(x,dtype=float)
# print(a)
# frombuffer 用于实现动态数组

# s = 'hello world'.encode()
#
# a = np.frombuffer(s,dtype = 'S1')
# print(a)

# fromiter 方法从可迭代对象中创建ndarray对象返回一维数组

list = range(5)
it = iter(list)

x = np.fromiter(it,dtype=float)
print(x)
