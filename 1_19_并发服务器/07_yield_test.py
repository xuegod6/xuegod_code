# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 22:22
# @Author  : for 
# @File    : 07_yield_test.py
# @Software: PyCharm
import sys,time,gevent
from gevent import socket,monkey
#打补丁 让gevent识别延迟操作
monkey.patch_all()
def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:#如果没有数据
            conn.close()#关闭信道
            break#强制break
        print('recv',data.decode())#打印信息
def server(port):
    s = socket.socket()
    s.bind(('127.0.0.1',port))
    s.listen(5)
    while True:
        cli,addr = s.accept()
        #开启协程处理任务
        gevent.spawn(handle_request,cli)
if __name__ == '__main__':
    server(8080)