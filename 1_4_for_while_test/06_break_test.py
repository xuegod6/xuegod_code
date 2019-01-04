# -*- coding: utf-8 -*-
# @Time : 2019/1/4 22:27 
# @Author : for 
# @File : 06_break_test.py 
# @Software: PyCharm
# name = 'xuegod'
#
# for i in name:
#     if i =='e':
#         continue
#     print(i,end='')
# exit()
result = [i for i in range(10)if i % 2 ==0 ]
print(result)

result1 = []
for i in range(10):
    if i%2 == 0:
        result1.append(i)
print(result1)
for i in {'name':'for','age':18}:
    print(i)

dic2 ={k:v for k,v in {'name':'for','age':18}.items()}
# print(dic2)
L = [1,2,3,1,2,3,4]
set1 = {i for i in L}
print(set1)
