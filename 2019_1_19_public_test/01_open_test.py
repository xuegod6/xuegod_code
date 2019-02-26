# -*- coding: utf-8 -*-
# @Time : 2019/1/19 10:05 
# @Author : for 
# @File : 01_open_test.py 
# @Software: PyCharm
#read
f = open('by.txt','r',encoding='utf-8')
content = f.read()
print(content)
f.close()