# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 22:00
# @Author  : for 
# @File    : 07_pro_tall_test.py
# @Software: PyCharm
import multiprocessing,time

def write_data(queue):
    for i in range(10):
        if queue.full():
            print('队列满了')
            break
        queue.put(i)
        time.sleep(0.2)
        print('写入的数据为:',i)
def read_data(queue):
    while True:
        if queue.qsize() == 0:
            print('队列空了')
            break
        value = queue.get()
        print('得到的数据',value)
if __name__ == '__main__':
    queue = multiprocessing.Queue(5)
    write_process = multiprocessing.Process(target=write_data,args=(queue,))
    read_process = multiprocessing.Process(target=read_data,args=(queue,))
    write_process.start()
    write_process.join()
    read_process.start()

