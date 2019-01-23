# -*- coding: utf-8 -*-
# @Time : 2019/1/22 22:06 
# @Author : for 
# @File : 06_with_test.py 
# @Software: PyCharm
# with open('2.txt','r',encoding='utf-8') as f:
# #     print(f.read())
# # print(f.closed)
#with 原理展示
# class A:
#     def __enter__(self):
#         print('__enter__() is called')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('__exit__() is called ')
# with A() as a:
#     print('got instance')

#对图片文件操作
with open('for.png','rb') as png1:
    with open('shu.png','wb') as png2:
        png2.write(png1.read())

with open('for.png','rb') as png1, open('shu.png','wb') as png2:
    png2.write(png1.read())


