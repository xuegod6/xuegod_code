# -*- coding: utf-8 -*-
# @Time : 2018/12/24 14:05 
# @Author : for 
# @File : test.py 
# @Software: PyCharm

import random
a = (random.randrange(1,10)for i in range(5))
print(list(a))
# 把它张开就是
a = []
for i in range(5):
    a.append(random.randrange(10))
print(a)