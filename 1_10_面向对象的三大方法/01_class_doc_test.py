# -*- coding: utf-8 -*-
# @Time : 2019/1/19 20:35 
# @Author : for 
# @File : 01_class_doc_test.py 
# @Software: PyCharm
class Parent:
    '所有人类的基类'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_info(self):
        print('set_info')
    def print_info(self):
        print(self.name,self.age)

p = Parent('for',18)
p.print_info()
print('类的属性:',Parent.__dict__)
print('类的文档字符串：',Parent.__doc__)
print('类姓名:',Parent.__name__)
print('类定义所在的模块:',Parent.__module__)
print('类的所有的父类的构成元素',Parent.__bases__)