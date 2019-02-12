# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 10:24
# @Author  : for 
# @File    : 03_gevent_test.py
# @Software: PyCharm
# import gevent
# def work(n):
#     for i in range(n):
#         print(gevent.getcurrent(),i)
#         gevent.sleep(1)
# g1 = gevent.spawn(work,5)
# g2 = gevent.spawn(work,5)
# g3 = gevent.spawn(work,5)
# g1.join()
# g2.join()
# g3.join()

import gevent,time
from gevent import monkey
#打补丁，让咱们的gevent识别 好时代操作，time.sleep.网络请求延迟
monkey.patch_all()
def work1(num):
    for i in range(num):
        print('work1')
        time.sleep(0.2)
def work2(num):
    for i in range(num):
        print('work2')
        time.sleep(0.2)
if __name__ == '__main__':
    g1 = gevent.spawn(work1,3)
    g2 = gevent.spawn(work2,3)
    g1.join()
    g2.join()






















