# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 21:17
# @Author  : for 
# @File    : 01_ziP_test.py
# @Software: PyCharm
numbers = [10086,10000,10010,95558]
names = ['中国移动','中国电信','中国联通']
#x,y = (10086,'中国移动')
for x,y in zip(numbers,names):
    print(y,'客服电话是:',x)

