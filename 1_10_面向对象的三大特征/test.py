# -*- coding: utf-8 -*-
# @Time : 2019/1/18 16:13 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
# class Parent:
#     '所有人类的基类'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def set_info(self):
#         print('set_info')
#     def print_info(self):
#         print(self.name,self.age)
# p = Parent('for',18)
# p.print_info()
# print('类的属性',Parent.__dict__)
# print('类的文档字符串',Parent.__doc__)
# print('类的姓名',Parent.__name__)
# print('类定义所在的模块',Parent.__module__)
# print('类的所有父类构成的元素',Parent.__bases__)
#
# class People(object):
#     #类属性
#     country = 'china'
# #类方法，用classmethod来进行修饰
#     @classmethod
#     def getCountry(cls):
#         return cls.country
# p = People()
# print(p.getCountry())      # 可以用做实例对象引用
# print(People.getCountry()) # 可以通过类对象引用

# class People(object):
#     #类属性
#     country = 'china'
#     #类方法，用classmethod来进行修饰
#     @classmethod
#     # cls 用来接收类对象例如：People
#     def getCountry(cls):
#         return cls.country
#     @classmethod
#     # cls 用来接收类对象例如：People
#     def setCountry(cls,country):
#         #更改类属性，People.country = country
#         cls.country = country
# p = People()
# #可以用过实例对象引用
# print (p.getCountry())
# #可以通过类对象引用
# print (People.getCountry())
# #更改类属性为japan
# p.setCountry('japan')
# #可以用过实例对象引用
# print (p.getCountry())
# #可以通过类对象引用
# print (People.getCountry())


# class People(object):
#     country = 'china'
#     @staticmethod#静态方法
#     def getCountry():
#         print(People.country)
#     def test(self):
#         print(self.country)
# #类对象访问静态方法
# People.getCountry()
# #实例化一个对象
# P = People()
# #调用静态方法
# P.getCountry()
# #调用实例方法
# P.test()

# class Game:
#     def __init__(self,player_name):
#         self.player_name = player_name
# #类对象直接调用
#         Game.show_help()
#         Game.show_top_score()
# #静态方法
#     @staticmethod
#     def show_help():
#         print('--------------')
#         print('|查看帮助信息|')
#         print('--------------')
# #类方法
#     @classmethod
#     def show_top_score(cls):
#         print('--------------')
#         print('|最高分数:1111|')
#         print('--------------')
#     def start_name(self):
#         print('%s开始游戏'%(self.player_name))
# tom = Game('for')
# tom.start_name()


# class Parent:
#     #私有类属性
#     __age= 10
#     def hello(self):
#         print(Parent.__age)
# p = Parent()
# p.hello()
# print(Parent.__age)

# class Parent:
#     def __init__(self,name,age):
#         self.__name = name
#         self.age = age
#     def hello(self):
#         print(self.__name)
# #创建P这个对象
# P = Parent('xuegod',18)
# #调用对象的属性
# P.hello()	# 可以
# print(P.__name) #报错
#
# class Parent:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def __func(self):
#         print('我是私有实例方法')
#     def hello(self):
#         self.__func()
# #创建P这个对象
# P = Parent('xuegod',18)
# #调用对象的属性
# P.hello()  	#可以
# P.__func()	#报错

#coding = utf-8
# class Parent:
#     '人类文档说明'
#     sex = '男'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# 	#通过利用self间接调用
#     def print_info(self):
#         print(self.name,self.age)
#
# For = Parent('for',18)
# #通过对象直接调用
# print(For.name,For.age,For.sex)
# For.print_info()


# class Animal:
#     def eat(self):
#         print('吃……')
#     def drink(self):
#         print('喝……')
# class Dog(Animal):
#     def eat(self):
#         print('狗吃……')
#     def call(self):
#         print('汪汪叫……')
# class Cat(Animal):
#     def catch(self):
#         print('抓老鼠……')
# #实例化一个对象
# dog = Dog()
# #调用父类的方法
# dog.eat()
# tom = Cat()
# tom.eat()
# #调用对象本身的方法
# tom.catch()
#
#
# class Animal:
#     def __init__(self,name='动物',color = '黄色'):
#         self.__name = name
#         self.color =color
#     def eat(self):
#         print('吃……')
#     def drink(self):
#         print('喝……')
#     def __test(self):
#         print(self.color)
#     def print_func(self):
#         print(self.__name)
#         print(self.color)
# class Dog(Animal):
#     def eat(self):
#         print('狗吃……')
#     def call(self):
#         print('汪汪叫……')
#
# #实例化一个对象
# dog = Dog()
# #访问父类的方法
# dog.drink()
# #访问父类的私有方法
# dog.__test()		#报错
# #调用父类的属性
# print(dog.color)
# print(dog.__name)#报错


class Dog(object):
    def print_self(self):
        print('11111')
class Tom(Dog):
    def print_self(self):
        print('2222')
def func(object):
#定义时的类型不知道调用哪个类方法，当运行的时候才确定调用哪个方法，这种情况我们叫做多态
    object.print_self()
# dog = Dog()
# fuc(dog)
tom = Tom()
#调用
func(tom)
