# -*- coding: utf-8 -*-
# @Time : 2019/1/7 22:27 
# @Author : for 
# @File : 06_zuoyongyu_test.py 
# @Software: PyCharm

# import sys
# # 得到所有该模块的方法 内建作用域
# print(dir(sys))
# # 全局
# name = 'while'
# def hello():
#     # name = 'for'#嵌套
#     def hi():
#         #本地作用域
#         # name = 'xiao'
#         age = 18
#         print(name)
#         print(age)
#     hi()
# hello()
#
# #global 声明全局变量
# name = 'for'
# print(name)
# def hello():
#     # name = 'while'
#     global name
#     name = name + ' is cool'
#     print(name)
# # hello()
# # print(name)
#
# c = [1,2,3]
# d = {}
# e = set()
# def test01():
#     c.append('5')
#     d.update({'name':'for'})
#     e.add(1)
# test01()
# print(c,d,e)
import functools
def add(a, b):
    return a + b
# add(4, 2)
#利用偏导数给一个固定值
plus3 = functools.partial(add, 3)
plus5 = functools.partial(add, 5)
print(plus3(2))
print(plus5(3))
