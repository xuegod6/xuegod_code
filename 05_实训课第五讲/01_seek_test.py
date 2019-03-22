# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 21:29
# @Author  : for 
# @File    : 01_seek_test.py
# @Software: PyCharm
# f = open('1.py','r+',encoding='utf-8')
# # # # #
# # # # # print(f.read(2))
# # # # #
# # # # # print('指针指向：',f.tell())
# # # # #
# # # # # f.write('uuuuuuu')
# # # # #
# # # # # f.write('111')
# # # # #
# # # # # f.close()






f = open('1.txt','r+',encoding='gbk')
print(f.name)
#读取一行
line = f.readline()
line = f.readline()
print(line)
#获取为你家指针当前的位置
pos = f.tell()
print('当前只针的位置%s'%pos)
#关闭
f.close()











