# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 15:21
# @Author  : for 
# @File    : 03_log_test.py
# @Software: PyCharm
import datetime
def outer(func):
    def inner(*args,**kwargs):
        print('时间：%s,%s 开始处理(%s,%s)'%(datetime.datetime.now(),func.__name__,args,kwargs))
    return inner
@outer
def first():
    pass
@outer
def second(a,b,c):
    pass
if __name__ == '__main__':
    first()
    second(1,2,c=3)