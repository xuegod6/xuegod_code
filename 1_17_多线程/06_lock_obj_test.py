# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 22:17
# @Author  : for 
# @File    : 06_lock_obj_test.py
# @Software: PyCharm
import threading,time
num = 0
#创建一个锁
lock = threading.Lock()
class MYThread(threading.Thread):
    # def __init__(self):
    #     pass
    def run(self):
        #得到锁
        lock.acquire()
        global num
        time.sleep(1)
        num += 1
        msg = self.name + ' set num to ' + str(num)
        print(msg)
        #释放锁
        lock.release()
def test():
    for i in range(5):
        t = MYThread()
        t.start()
if __name__ == '__main__':
    test()