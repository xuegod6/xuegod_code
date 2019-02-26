# -*- coding: utf-8 -*-
# @Time : 2019/1/9 14:52 
# @Author : for 
# @File : 01_iter_test.py 
# @Software: PyCharm
L = [2,3,4,7]

# for x in L:
#     print(x)
# else:
#     print('循环结束')
it = iter(L)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print('循环结束')
        break