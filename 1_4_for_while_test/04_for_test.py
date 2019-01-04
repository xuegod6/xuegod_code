# -*- coding: utf-8 -*-
# @Time : 2019/1/4 21:48 
# @Author : for 
# @File : 04_for_test.py 
# @Software: PyCharm
for i in range(2,10,2):
    print(i,end='-')

name = 'xuegod'

for i in name:
    print(i)
# # print(i)
a= [(1,2),(3,4)]
for i in a:
    print(i[0])
i,j = (1,2)
for i,j in a:
    print('这是i %s'%i)
    print('这是j %s'%j)
#
for i in range(1,10):# i =1 i = 2
    for j in range(1,i+1):#(1,2) i1,2
        print('%d x %d = %d\t'%(j,i,i*j),end='')
    print()