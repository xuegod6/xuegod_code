# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 21:25
# @Author  : for 
# @File    : 03_thread_pro_test.py
# @Software: PyCharm4
# import threading,time
#
# def say(name):
#     print('%s is start'%name)
#     # time.sleep(3)
#     print('%s is stop'%name)
# if __name__ == '__main__':
#     print('主线程开始')
#     t = threading.Thread(target=say,args=('for',))
#     t.setDaemon(True)
#     t.start()
#     # time.sleep(4)
#     print('---主线程结束--')


#多个子线程

import threading,time

def say(name):
    print('%s is start'%name)
    time.sleep(1)
    print('%s is stop'%name)



def hello(name):
    print('%s is start'%name)
    time.sleep(2)
    print('%s is stop'%name)

if __name__ == '__main__':
    print('---主线程开始---')
    t1 = threading.Thread(target=say,args=('for',))
    t2 = threading.Thread(target=hello,args=('while',))

    t1.setDaemon(True)

    t1.start()
    t2.start()

    print('---主线程结束---')
