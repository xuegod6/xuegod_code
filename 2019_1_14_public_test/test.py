# -*- coding: utf-8 -*-
# @Time : 2019/1/14 10:10 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
# def myzip(*args):
#     all_list = []
#     for i in range(len(args)):
#         all_list.append(args[i])
#     sort_list = sorted(all_list,key=lambda x:len(x))
#     min_list_longth = len(sort_list[0])
#     print(min_list_longth)
#     a_list = []
#     for a in range(min_list_longth):#0,1,2
#         a = [args[j][a] for j in range(len(args))]
#         a_list.append(a)
#     print(a_list)
# myzip([1,2,3],[4,2],[1,3,4,5],[1,2,3,4,5,6])

#1-100
list1 = []
for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        list1.append(i)
print(list1)


