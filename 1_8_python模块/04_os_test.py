# -*- coding: utf-8 -*-
# @Time : 2019/1/15 22:20 
# @Author : for 
# @File : 04_os_test.py 
# @Software: PyCharm
import os
# print(os.sep)
# print(os.name)
# print(os.getcwd())#获取当前路径
# print(os.listdir('imp_test'))
# os.chdir()#b不提倡
# os.mkdir('for')
# os.makedirs('a/b/c')
# os.rmdir('for')
# os.removedirs('a/b/c')
# os.remove('test.py')
# a = 'mkdir nwdir'
# b = os.system(a)
# print(b)
a = 'mkdir ndir'
b = os.popen(a,'r',1)
print(b)












