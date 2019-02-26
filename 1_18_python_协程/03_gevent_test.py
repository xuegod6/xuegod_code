# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:01
# @Author  : for 
# @File    : 03_gevent_test.py
# @Software: PyCharm
import gevent
def work(n):
    for i in range(n):
        #获取当前的线程名字
        print(gevent.getcurrent().name,i)
        #利用协程的方法一秒
        gevent.sleep(1)
g1 = gevent.spawn(work,5)
g2 = gevent.spawn(work,5)
g3 = gevent.spawn(work,5)
g1.join()
g2.join()
g3.join()