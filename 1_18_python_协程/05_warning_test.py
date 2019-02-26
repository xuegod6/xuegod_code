# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:20
# @Author  : for 
# @File    : 05_warning_test.py
# @Software: PyCharm
import gevent
import time
from gevent import monkey

monkey.patch_all()

def work1(num):
    for i in range(num):
        print('---work1---')
        time.sleep(2)
def work2(num):
    for i in range(num):
        print('--work2--')
        time.sleep(2)
if __name__ == '__main__':
    #创建指定任务
    g1 = gevent.spawn(work1,3)
    g2 = gevent.spawn(work2,3)

    while True:
        print('主线程执行')
        time.sleep(0.5)