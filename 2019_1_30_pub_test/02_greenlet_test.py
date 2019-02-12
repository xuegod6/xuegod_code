# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 10:13
# @Author  : for 
# @File    : 02_greenlet_test.py
# @Software: PyCharm
import time,greenlet
def work1():
    for i in range(5):
        print('work1')
        time.sleep(0.2)
        g2.switch()
def work2():
    for i in range(5):
        print('work2')
        time.sleep(0.2)
        g1.switch()

if __name__ == '__main__':
    #创建协程指定一个任务
    g1 = greenlet.greenlet(work1)
    #创建协程指定一个任务
    g2 = greenlet.greenlet(work2)
    #切换到袄第一个协程执行对应的任务
    g1.switch()