# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 20:49
# @Author  : for 
# @File    : 02_greenlet_test.py
# @Software: PyCharm
import time
import greenlet

def work1():
    for i in range(5):
        print('---work---')
        time.sleep(0.2)
        #切换到第二个协程对应任务
        g2.switch()
def work2():
    for i in range(5):
        print('---work2---')
        time.sleep(0.2)
        #切换到第一个协程对应的任务
        g1.switch()

if __name__ == '__main__':
    g1 = greenlet.greenlet(work1)
    g2 = greenlet.greenlet(work2)
    #切换到第一个协程执行对应任务
    g1.switch()








