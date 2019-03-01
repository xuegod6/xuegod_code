# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:04
# @Author  : for 
# @File    : 03_demjson_test.py
# @Software: PyCharm
import demjson

s =  '{a:"000001_Unit_1. Hi,Birdie.mp3",b:"000005_Unit_2. Good morning,Miss Wang..mp3",c:"000008_Unit_3. What\'s your name_.mp3"}'
data1 = demjson.decode(s)
print(data1)
data2 = demjson.encode(data1)
print(data2)
print(type(data2))


