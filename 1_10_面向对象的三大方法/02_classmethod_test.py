# -*- coding: utf-8 -*-
# @Time : 2019/1/19 20:49 
# @Author : for 
# @File : 02_classmethod_test.py 
# @Software: PyCharm
# class People(object):
#     #类属性
#     country = 'china'
#     @classmethod#类方法
#     def getCountry(cls):
#         return cls.country
#     @classmethod
#     def setCountry(cls,country):
#         cls.country = country
# p = People()
# print(p.getCountry())
# print(People.getCountry())
# p.setCountry('japan')
# print(p.getCountry())
# print(People.getCountry())
#staticmethod
class People(object):
    #类属性
    country = 'china'
    #静态方法 没有cls 进性承载类对象 所以知己而通过 类对象进行访问
    @staticmethod
    def __getCountry():
        print(People.country)
    def test(self):
        People.__getCountry()
People.__getCountry()
P = People()
# P.getCountry()
P.test()


