# -*- coding: utf-8 -*-
# @Time : 2019/1/10 11:33 
# @Author : for 
# @File : 05_test.py 
# @Software: PyCharm
list1=[1,2,3]
list2=[4,5,6,0]
list3=[7,8,9]
L=[]
#L=zip(list1,list2,list3)
#print(list(L))
def zip_rewrite(*args):
    list1 = []
    if len(args)>0:
        for i in range(len(args)):
            list1.append(args[i])
        print(list1)
        # a = sorted(key=lambda x:len(x))
        # print(a)
    else:
        print("参数不能为空")
# zip_rewrite(list1,list2,list3)
# a = sorted()
a = [[1, 2], [4], [7, 8, 9,1,1]]
b = sorted(a,key=lambda x:len(x))
print(b)
# L = lambda x : len(x)