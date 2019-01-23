# -*- coding: utf-8 -*-
# @Time : 2019/1/22 22:19 
# @Author : for 
# @File : 07_tell_seek_test.py 
# @Software: PyCharm
# f = open('1.txt','r+',encoding='gbk')
# # # print(f.name)
# # # #赌气一行
# # # line = f.readline()
# # # print(line)
# # # #获取为你家指针当前的位置
# # # pos = f.tell()
# # # print('当前只针的位置%s'%pos)
# # # #关闭
# # # f.close()


f = open('1.txt','r+',encoding='gbk')
print(f.name)
#赌气一行
line = f.readline()
print(line)
f.seek(0,0)
print(f.readline())
#获取为你家指针当前的位置
pos = f.tell()
print('当前只针的位置%s'%pos)
#关闭
f.close()