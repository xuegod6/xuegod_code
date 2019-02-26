# -*- coding: utf-8 -*-
# @Time : 2019/1/15 22:08 
# @Author : for 
# @File : 03_time_test.py 
# @Software: PyCharm
import time
# print(time.localtime())
# print(time.gmtime())
# print(time.asctime())
# print(time.ctime())
# print(time.time())
# print(time.mktime(time.localtime()))
# print(time.clock())
# time.sleep(2)
print(time.strftime('%Y-%m-%d',time.localtime()))
print(time.strftime('%y-%m-%d',time.gmtime()))