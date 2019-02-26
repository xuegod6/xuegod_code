# -*- coding: utf-8 -*-
# @Time : 2019/1/19 10:22 
# @Author : for 
# @File : 02_wirte_test.py 
# @Software: PyCharm
# f = open('3.txt','a')
# f.write('hello\n')
# f.close()
# f = open('4.txt','w')
# f.write('for,django')
# f.close()

# f = open('4.txt','w')
# f.close()
# f.writelines(['a','b','c','d'])

with open('4.txt','w') as f:
    f.writelines(['a','b','c','d'])

