# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 22:09
# @Author  : for 
# @File    : 05_obj_threading_test.py
# @Software: PyCharm
import threading,time
num = 0
#面向对象家角度进行线程讲解
#继承线程的相对应的类
class MyThread(threading.Thread):
    #run方法是自带的相当于线程的运行
    def run(self):
        #指定说明全局变量
        global num
        time.sleep(1)
        #群居变量进行自增
        num += 1
        #selfname 代表一个子线程实例  threading_current_thread().name
        msg = self.name + ' set num to ' + str(num)
        print(msg)
def test():
    for i in range(5):
        #创建线程实例
        t = MyThread()
        #开启线程
        t.start()
if __name__ == '__main__':
    test()
