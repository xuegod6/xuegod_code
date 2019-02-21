# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 22:26
# @Author  : for 
# @File    : 07_queue_test.py
# @Software: PyCharm
import queue
Q = queue.Queue(10)
Q.put(1)
print(Q.empty())
data = Q.get()
print(data)