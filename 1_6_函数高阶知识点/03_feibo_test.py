# -*- coding: utf-8 -*-
# @Time : 2019/1/11 20:54 
# @Author : for 
# @File : 03_feibo_test.py 
# @Software: PyCharm
# def feibo(n):
#     a,b = 0,1
#     c = []
#     while n > 0:
#         c.append(b)
#         a,b = b,a+b
#         n -= 1
#     print(c)
# feibo(5)
# def fetbo(n):
#     if n <= 1:
#         return n
#     elif n==2:
#         return 1
#     return (fetbo(n-1) + fetbo(n-2))
#
# n = int(input('>>>')) # n = 4
# a = [fetbo(i)for i in range(1,n+1)]# i = 1,2,3,4   lsit = [1,1,2,3]
# print(a)