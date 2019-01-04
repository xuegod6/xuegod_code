# -*- coding: utf-8 -*-
# @Time : 2019/1/4 21:27 
# @Author : for 
# @File : 03_two_if_test.py
# @Software: PyCharm
num = 10
if num < 30:
    print('< 30')
elif num < 100:
    print(' < 100')

if num < 30:
    print('< 30')
if num < 100:
    print('< 100')
num = 18

if num < 15:
    if num > 8:
        print('15 > num > 8')
else:
    print('111')
    if num < 30:
        print('15 < num < 30')











