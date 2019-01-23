# -*- coding: utf-8 -*-
# @Time : 2019/1/22 20:56 
# @Author : for 
# @File : 03_str_test.py 
# @Software: PyCharm
class Test(object):
    def __init__(self,world):
        self.world = world
    def __str__(self):
        print('__str__')
        return 'world is %s'%self.world
t = Test('for')
# print(str(t))
print(t)