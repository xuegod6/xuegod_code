# -*- coding: utf-8 -*-
# @Time : 2019/1/17 21:09 
# @Author : for 
# @File : 02_class_test.py 
# @Software: PyCharm

# class Cat():
#     print('我是喵咪')
# #实例化一个tom对象
# tom = Cat()

# class Cat():
#     '我是喵咪'
#     def eat(self):
#         '猫'
#         print('猫在吃……')
#     def drink(self):
#         print('猫仔喝水……')
#     def print_info(self):
#         print('%s 的年龄是%s'%(tom.name,tom.age))
# #创建一个tom实例化对象
# tom = Cat()
# #调用实例方法
# tom.eat()
# tom.drink()
# #通过雷鸣调用实例方法
# Cat.eat(tom)
# tom.name = '汤姆'
# tom.age = 18
# tom.print_info()
# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# lucky = Cat()
# lucky.eat()
# lucky.drink()
# lucky.name = '幸运'
# lucky.age = 18
# lucky.print_info()

# class Bird:
#     def hello(self):
#         print(self)
# b = Bird()
# print(b)
# b.hello()
# Bird.hello(b)
#
#
# c = Bird()
# print(c)
# # c.hello()
#
#
#
# class Cat():
#     def __init__(self):
#         print('__init__被调用了')
#     def eat(self):
#         print('猫在吃……')
#     def drink(self):
#         print('猫仔喝水……')
#     def print_info(self):
#         print('%s 的年龄是%s'%(self.name,self.age))
# #实例化对对象
# tom = Cat()
# tom.name = '汤姆'
# tom.age = 18
# tom.print_info()
#经典类
# class Cat:
# class Cat():
# #新式类
# class Cat(object):










class Cat():
    def __init__(self):
        self.name = '汤姆'
        self.age = 18
    def eat(self):
        print('猫在吃……')
    def drink(self):
        print('猫仔喝水……')
    def print_info(self):
        print('%s 的年龄是%s'%(self.name,self.age))
#实例化对对象
tom = Cat()
tom.print_info()

