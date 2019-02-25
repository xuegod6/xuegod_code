# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 20:45
# @Author  : for 
# @File    : 01_client_test.py
# @Software: PyCharm
import socket
def work(i):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',8080))
    sock.send('我是client'.encode())
    sock.close()
    pass
for i in range(5):
    work(i)
