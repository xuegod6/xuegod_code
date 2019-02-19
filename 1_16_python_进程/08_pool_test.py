# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 22:10
# @Author  : for 
# @File    : 08_pool_test.py
# @Software: PyCharm
import multiprocessing,time

def work():
    print('复制中……',multiprocessing.current_process().pid)
    time.sleep(0.5)
if __name__ == '__main__':
    #3 进程池最大的个数
    pool = multiprocessing.Pool(3)
    for i in range(5):
        # 循环让进程池执行对应的work任务
        # 同步执行任务，一个任务执行完成以后另外一个任务才能执行
        # pool.apply(work)
        pool.apply_async(work)
    pool.close()
    #主进程等待进程池执行完毕之后再推出
    pool.join()