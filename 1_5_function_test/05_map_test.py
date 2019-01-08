# -*- coding: utf-8 -*-
# @Time : 2019/1/7 22:00 
# @Author : for 
# @File : 05_map_test.py 
# @Software: PyCharm
# a  = [1,2,3,4]
# b = []
# #返回平方
# def func(x):
#     return  x*x
# #遍历执行
# for i in a:
#     b.append(func(i))#重复调用
# print(b)
#map_test

# def func(x):
#     return x * x
#
# a = map(func,[1,2,3,4])
# print(list(a))
# # print(a)
# # for i in a:
# #     print(i,end='')

#lambada 如何实现
# b = map(lambda x : x*x,[1,2,3,4])
# print(b)
# a = [1,2,3]
# b = [4,5,6]
# c = map(lambda x,y:x+y,a,b)# a,b 内地元素分别传递给x，y
# print(list(c))
# # print(a+b)
# print(list(c))

#zip演示
a = [1,2,3,4]
b = [5,6,7]
c = zip(a,b)
print(c)
print(list(c))#强制转换
print(list(c))






