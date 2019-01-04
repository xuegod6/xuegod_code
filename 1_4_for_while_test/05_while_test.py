# -*- coding: utf-8 -*-
# @Time : 2019/1/4 22:13 
# @Author : for 
# @File : 05_while_test.py 
# @Software: PyCharm
while True:
    print('风中一匹狼')

a = 0
while a <10:
    print(a)
    a += 1

# i = 6
# while i > 5:
#     print('我是for')
# else:
#     print('我不是for')
n = int(input('请输入你想要的数字'))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print('*',end='')
        j += 1
    print()
    i += 1











