# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 21:51
# @Author  : for 
# @File    : 03_while_test.py
# @Software: PyCharm
num = int(input('请输入一个整数:'))

for i in range(1,num+1):
    print(' '* (num - i) + (2*i - 1)*'*')
a = num
while a > 0:
    print((num- 1)*' '+'*')
    a -= 1
