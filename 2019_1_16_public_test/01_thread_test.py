# -*- coding: utf-8 -*-
# @Time : 2019/1/16 11:18 
# @Author : for 
# @File : 01_thread_test.py 
# @Software: PyCharm
# import _thread
# # import time
# # # 为线程定义一个函数
# # def print_time( threadName, delay):
# #    count = 0
# #    while count < 5:
# #       time.sleep(delay)
# #       count += 1
# #       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# # # 创建两个线程
# # #但是这个模块我们不推荐，因为底层封装的时候它的主线程不会等待子线程的结束！
# # #官方以及我们推荐再封装Threading，所以在这里大家了解下
# # try:
# #    _thread.start_new_thread( print_time,("Thread-1", 2, ) )
# #    _thread.start_new_thread( print_time,("Thread-2", 4, ) )
# # except:
# #    print ("Error: 无法启动线程")
# # while True:
# #     pass

import threading
import time
def run(number):
    print('%s…… starting '%number)
    time.sleep(2)
    print('____________')
if __name__ == '__main__':
    print('___主线程开始___',threading.current_thread().name)
    thread_list=[]
    for i in range(1,5):
        #创建，实例化一个线程
        t = threading.Thread(target= run,args=(i,))
        thread_list.append(t)
  #将实例化的线程都放到列表中，统一执行
    for t in thread_list:
        t.start()
        t.join()
    print('___主线程结束___',threading.current_thread().name)

