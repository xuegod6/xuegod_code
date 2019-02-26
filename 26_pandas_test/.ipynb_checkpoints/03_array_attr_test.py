# -*- coding: utf-8 -*-
# @Time : 2018/12/28 10:52 
# @Author : for 
# @File : 03_array_attr_test.py 
# @Software: PyCharm
import numpy as np

a = np.arange(24)

# print(a)
# print(a.ndim)

# b= a.reshape(2,4,3)
# print(b.ndim)
#弄清楚数组的维数
# a = np.array([[[1,2,3],[4,5,6]]])
# a.shape = (3,2)
# print(a)
# print(a.ndim)
# ndarray.itemsize
# 数组中每个元素的大小
# x = np.array([1,2,3,4,5],dtype=np.int8)
# print(x.itemsize)
# y  = np.array([1,2,3,4,5],dtype = np.float64)
# print(y.itemsize)
#flag 打印出对象的内存信息，很多属性
x = np.array([1,2,3,4,5])
print(x.flags)
