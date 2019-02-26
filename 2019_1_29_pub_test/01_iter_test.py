# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 14:45
# @Author  : for 
# @File    : 01_iter_test.py
# @Software: PyCharm
# L = [2,3,5,7]
# it = iter(L)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# it = iter(range(1,10,3))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for i in range(1,5,2):
#     print(i)
# L = [2,3,5,7]
# for x in L:
#     print(x)
# else:
#     print('循环结束')
# it = iter(L)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         print('循环结束')
#         break


# 练习:
# 有一个集合:s = {'唐僧', '悟空', '八戒', '沙僧'}
# 用 for语句来遍历所有元素如下:
# for x in s:
#     print(x)
# else:
#     print('遍历结束')
# 请将上面的for语句改写为 while语句和迭代器实现？

s = {'唐僧', '悟空', '八戒', '沙僧'}
L = iter(s)
n = 0
while n < len(s):
    print(next(L))
    n += 1
else:
    print('遍历结束')





















