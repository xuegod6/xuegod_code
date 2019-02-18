# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 22:25
# @Author  : for 
# @File    : 05_socket_client.py
# @Software: PyCharm
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8000))
sock.send('client3'.encode())
print(sock.recv(521).decode())
sock.close()