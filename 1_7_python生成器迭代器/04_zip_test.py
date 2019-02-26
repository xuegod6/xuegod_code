# -*- coding: utf-8 -*-
# @Time : 2019/1/14 21:54 
# @Author : for 
# @File : 04_zip_test.py 
# @Software: PyCharm

numbers = [10086, 10000, 10010, 9558]
names = ['中国移动', '中国电信', '中国联通']


# def myzip(iter1,iter2):
#     it1 = iter(iter1)
#     it2 = iter(iter2)
#     while True:
#         a = next(it1)
#         b = next(it2)
#         yield (a,b)
# for t in myzip(numbers,names):
#     print(t)

# for t in zip(numbers,names):
#     print(t)
# for x,y in zip(numbers,names):
#     print(y,'的客服电话是:',x)
#
# x,y = (10086, '中国移动')

def myzip(*args):
    all_list = [] #
    for i in range(len(args)):
        all_list.append(args[i])
    print('这是all_list:',all_list)
    #我要利用你每个元素当中的长度进行排序
    sort_list = sorted(all_list,key=lambda x:len(x))
    print('这是排序结果:',sort_list)
    #得到最小的长度
    min_list_longth = len(sort_list[0])
    #定义一个空列表
    a_list = []

    for a in range(min_list_longth):#0,1
        #
        a = [args[j][a] for j in range(len(args))]#len(args) == 3 j == 0,1,2
        a_list.append(a)

    print(a_list)
myzip([1,2,3],[2,3,4,5],[1,2])





