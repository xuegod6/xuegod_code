# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 21:28
# @Author  : for 
# @File    : 02_UDP_client_test.py
# @Software: PyCharm
import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind(('127.0.0.1',8001))

sock.sendto('client'.encode(),('127.0.0.1',9099))

data,address = sock.recvfrom(521)

print(data.decode(),address)

sock.close()