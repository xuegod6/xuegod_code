# -*- coding: utf-8 -*-
# @Time : 2019/1/19 21:50 
# @Author : for 
# @File : 05_jicheng_test.py 
# @Software: PyCharm
class Animal(object):
    def __init__(self,name = '动物',color = '黄色'):
        self.__name = name
        self.color = color
    def eat(self):
        print('吃……')
    def drink(self):
        print('喝……')
    def __test(self):
        print(self.color)
    def print_func(self):
        print(self.__name)
        print(self.color)
class Dog(Animal):
    def eat(self):
        print('狗吃……')
    def call(self):
        print('旺旺叫')
    def print_info(self):

        print(self.__name)

dog = Dog()
dog.drink()
dog.eat()
# dog.__test()
# tom.call()
print(dog.color)
dog.print_info()