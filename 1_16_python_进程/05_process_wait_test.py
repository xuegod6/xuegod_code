# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 21:27
# @Author  : for 
# @File    : 05_process_wait_test.py
# @Software: PyCharm
import multiprocessing,time
def work():
    for i in range(10):
        print('工作中...')
        time.sleep(0.1)
if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.start()
    # work_process.join()
    time.sleep(2)
    print('主进程执行完毕')
    work_process.terminate()