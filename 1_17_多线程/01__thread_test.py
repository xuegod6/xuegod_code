# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 20:55
# @Author  : for 
# @File    : 01__thread_test.py
# @Software: PyCharm
import _thread,time

def print_time(threadName,delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s:%s'%(threadName,time.ctime(time.time())))

if __name__ == '__main__':
    #创建两个线程
    #这个模块我们不推荐，应为地城封装的时候它的主线程不会等待子线程的结束（非阻塞）！
    #官方说明我们不大推荐这个模块 我们退阿基诺这个模块的再傅恒装threading，
    try:
        _thread.start_new_thread(print_time,('Thread-1',2,))
        _thread.start_new_thread(print_time,('Thread-2',4,))
    except:
        print('Error:无法启动线程')
    while True:
        pass