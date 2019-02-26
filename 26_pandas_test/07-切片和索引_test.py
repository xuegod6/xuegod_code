# # -*- coding: utf-8 -*-
# # @Time : 2018/12/28 12:00
# # @Author : for
# # @File : 07-切片和索引_test.py
# # @Software: PyCharm
import numpy as np
#
# a = np.arange(10)
# #从2开始 7结束 2步长
# s = slice(2,7,2)
# print(a[s])
#
# a = np.arange(10)
# b = a[2:7:2]
# print(b)
# x = np.array([[1,2],[3,4],[5,6]])
# # print(x)
# y = x[[0,1,2],[0,1,0]]
# print((y))

# x = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
# print('我们的数组是：')
# print(x)
# print()
#
# print('大于五的元素')
# print(x[x>5])

# print('我们的数组是：')
# print(x)
# print()
# rows = np.array([[0,0],[3,3]])
# clos = np.array([[0,2],[0,2]])
#
# y = x[rows,clos]
# print(y)


# a = np.array([np.nan,1,2,np.nan,3,4,5])
# print(a[~np.isnan(a)])
# x = np.arange(32).reshape(8,4)
# print(x)
# print(x[[-4,-2,-1,-7]])