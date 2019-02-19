# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 20:54
# @Author  : for 
# @File    : 02_pid_test.py
# @Software: PyCharm
import multiprocessing,time,os

def work():
    #获取当前的进程
    cuttent_process = multiprocessing.current_process()
#回去当前的工作进程
    print('目前工作的:',cuttent_process)
#获取当前的进程 id
    print('当前进程编号：',cuttent_process.pid,os.getpid())
#获取父进程的编号
    print('父进程的编号:',os.getppid())
#随2秒
    time.sleep(2)

if __name__ == '__main__':

    current_process = multiprocessing.current_process()

    print('main:',current_process)

    print('main进程的编号：',current_process.pid)
    #阿克齐尼子进程
    sub_process = multiprocessing.Process(target=work)
    sub_process.start()

    print('主进程结束')

