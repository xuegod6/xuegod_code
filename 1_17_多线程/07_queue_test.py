# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 22:26
# @Author  : for 
# @File    : 07_queue_test.py
# @Software: PyCharm
a = 'abdsafegfagaweggadge'

a_dict = {}
b = set(a)
for i in b:
    count_a = a.count(i)
    a_dict[i] = count_a
print(a_dict)