# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 21:19
# @Author  : for 
# @File    : 02_with_test.py
# @Software: PyCharm
# with open('1.txt','r',encoding='gbk') as f:
#     print(f.read())
# print(f.closed)

with open('0.jpg','rb') as png1:

    with open('1.jpg','wb') as png2:

        png2.write(png1.read())


with open('0.jpg','rb') as png1,open('1.jpg','wb') as png2:

    png2.write(png1.read())