# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 15:21
# @Author  : for 
# @File    : 03_zip_test.py
# @Software: PyCharm
# numbers = [10086, 10000, 10010, 9558]

# for x,y in zip(numbers,names):
#     print(y,'的客服电话是',x)
# a,b= (1,2)
# print(a)
# print(b)
# def myzip(iter1,iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     while True:
#         a = next(it1)
#         b = next(it2)
#         yield (a,b)
# for t in myzip(numbers,names):
#     print(t)



class A(object):
    def create(self,request,format = None):
        pass
class B(A):
    def create(self,request,format = None):
        return super().create(request.format)

b = B()
b.create('1',6)
print(b.__class__.__mro__)




# names = ['中国移动', '中国电信', '中国联通']
# # for t in enumerate(names,1):
# #     print(t)
# def myenum(iterable):
#     it = iter(iterable)
#     i = 0
#     while True:
#         a = next(it)
#         yield (i,a)
#         i += 1
# for i in myenum(names):
#     print(i)


