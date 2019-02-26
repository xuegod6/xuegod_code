# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:11
# @Author  : for 
# @File    : 04_monkey_test.py
# @Software: PyCharm
import gevent
import time
from gevent import monkey
#打补丁，让gevent框架识别还是操作，比如：time.sleep()
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

    g1.join()
    g2.join()

