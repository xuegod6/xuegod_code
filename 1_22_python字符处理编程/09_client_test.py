# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 22:22
# @Author  : for 
# @File    : 09_client_test.py
# @Software: PyCharm
import socket,time
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8000))
while True:
    sock.send(b'hello I am client001')
    time.sleep(1)
    recv = sock.recv(521)
    print(recv)
sock.close()
