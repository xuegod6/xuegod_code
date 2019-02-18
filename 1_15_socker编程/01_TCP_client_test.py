# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 21:18
# @Author  : for 
# @File    : 01_TCP_client_test.py
# @Software: PyCharm
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(('127.0.0.1',9000))

print(sock.recv(521).decode())

sock.send('Hi'.encode())

sock.close()