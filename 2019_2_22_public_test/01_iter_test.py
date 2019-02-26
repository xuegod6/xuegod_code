# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:16
# @Author  : for 
# @File    : 01_iter_test.py
# @Software: PyCharm
# L = [2,3,5,7]
#for循环
# for x in L:
#     print(x)
# else:
#     print('循环结束')

#iter方法
# it = iter(L)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         print('循环结束')
#         break

###########################################




L = [2,3,5,7]
s = iter(L)
n = 0
while n < len(L):
    print(next(s))
    n += 1
else:
    print('遍历结束')








