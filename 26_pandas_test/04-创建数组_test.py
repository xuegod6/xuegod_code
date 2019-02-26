# -*- coding: utf-8 -*-
# @Time : 2018/12/28 11:11 
# @Author : for 
# @File : 04-创建数组_test.py 
# @Software: PyCharm
# enmpty方法指定创建一个指定形状 数据类型的企鹅没有初始化的数组
import numpy as np
#empty 方法指定形状
# x = np.empty([3,2],dtype=int)
# print(x)

# zeros创建指定大小的数组数组的元素以0来填充
# x = np.zeros(5)
# print(x)
# x = np.zeros((5,),dtype=np.int)
# print(x)
#
# z = np.zeros((2,2),dtype=[('x','i4'),('y','i4')])
# print(z)

# ones = 创建指定的形状的数组，数组的元素以1来填充
# x = np.ones(5)
# print(x)
# x= np.ones([2,2],dtype=int)
# print(x)

# 创建标准的正态分布数组
# from numpy import *
# a = random.randn(2,3)
# print(a)

from numpy import *

a = random.randint(100,200,(3,3))
print(a)

