# -*- coding: utf-8 -*-
# @Time : 2019/1/14 21:04 
# @Author : for 
# @File : 02_iter_test.py 
# @Software: PyCharm
# L = [2,3,5,7]
# # #创建一个it迭代器 参数是可迭代对象
# # it = iter(L)
# # # print(it)
# # print(next(it))#next方法让他指向不同的数值
# # print(next(it))
# # print(next(it))
# # print(next(it))
# # print(next(it))#没有 就会出现stopiteration

# it = iter(range(1,10,3))
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

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
s = {'唐僧', '悟空', '八戒', '沙僧'}
for i in s:
    print(i)
else:
    print('遍历结束')


L = iter(s)
n = 0
while n < len(s):
    print(next(L))
    n += 1
else:
    print('遍历结束')