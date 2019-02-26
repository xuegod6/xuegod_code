# -*- coding: utf-8 -*-
# @Time : 2019/1/10 15:13 
# @Author : for 
# @File : 06_rhce_test.py 
# @Software: PyCharm
def outer():
    def inner():
        print('我是inner')
    return inner
outer()()