# -*- coding: utf-8 -*-
# @Time : 2018/12/29 16:41 
# @Author : for 
# @File : 09-迭代数组_test.py 
# @Software: PyCharm
import numpy as np
# a = np.arange(6).reshape(2,3)
#
# for x in np.nditer(a.T):
#     print(x,end=',')
# print('\n')
#
# for x in np.nditer(a.T.copy(order='C')):
#     print(x,end=',')


# for x in np.nditer


#控制便利的顺序

a = np.arange(0,60,5)

a = a.reshape(3,4)

print('原始数组：')
print(a)

print('原始数组的转置是：')
b = a.T
print(b)
print('以C的风格排序：')
c = b.copy(order='C')
print(c)

for x in np.nditer(c):
    print(x,end=',')
c = b.copy(order='F')
print(c)

for x in np.nditer(c):
    print(x,end=',')
    
