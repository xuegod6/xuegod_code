# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 21:57
# @Author  : for 
# @File    : 04_list_threadIng_test.py
# @Software: PyCharm
import threading,time
def run(number):
    print('%s....starting'%number)
    time.sleep(2)
    print('---------')
if __name__ == '__main__':
    print('----主线程开始---',threading.current_thread().name)
    thread_list = []
    #创建一个个实例化线程
    for i in range(1,5):
        t = threading.Thread(target=run,args=(i,))
        thread_list.append(t)
    #线程统一执行
    for t in thread_list:
        t.start()
        t.join()

    print('----主线程结束---',threading.current_thread().name)