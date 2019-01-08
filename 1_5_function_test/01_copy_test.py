# -*- coding: utf-8 -*-
# @Time : 2019/1/7 20:36 
# @Author : for 
# @File : 01_copy_test.py 
# @Software: PyCharm
import copy

a = [1,2,3,4,[5,6,7]]

b = a

print('a 的 id : %s ,b 的 Id %s '%(id(a),id(b)))
#深copy
d = copy.deepcopy(a)
print('d 的 id',id(d))
#浅copy
c = copy.copy(a)
print(id(c))

a.append(8)
a[4].append(9)

print(a)
print(b)
print(c)#浅
print(d)#深的


