# -*- coding: utf-8 -*-
# @Time : 2019/1/5 10:17 
# @Author : for 
# @File : 07_iter_test.py 
# @Software: PyCharm
L = [2,3,5,7]
#
# for x in L:
#     print(x)
# else:
#     print('循环结束')
it = iter(L)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         print('循环结束')
#         break


s = {'唐僧', '悟空', '八戒', '沙僧'}
# for x in s:
#     print(x)
# else:
#     print('遍历结束')


L = iter(s)
n = 0
while n < len(s):
    print(next(L))
    n += 1
else:
    print('遍历结束')

