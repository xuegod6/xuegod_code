# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 21:11
# @Author  : for 
# @File    : 02_threading_test.py
# @Software: PyCharm
import threading,time
def say(name):
    print('first start time %s'%time.ctime())
    print('你好%s'%name)
    time.sleep(3)
    print('first stop time %s'%time.ctime())
def hello(name):
    print('second start time %s'%time.ctime())
    print('你好%s'%name)
    time.sleep(3)
    print('second stop time %s'%time.ctime())
def main():
    print('我是main')

if __name__ == '__main__':
    print('--主线程开始--',threading.current_thread().name)
    #设置3个子线程
    t1 = threading.Thread(target=say,args=('for',))
    t2 = threading.Thread(target=hello,args=('while',))
    t3 = threading.Thread(target=main,args=())
    #给一个t1 线程起一个名字
    t1.setName('越努力，越幸福')
    #启动线程
    t1.start()
    #得到并打印线程
    print(t1.getName())
    t2.start()
    t3.start()
    print('--主线程结束--',threading.current_thread().name)