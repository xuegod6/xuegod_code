# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 21:25
# @Author  : for 
# @File    : 02_UDP_server_test.py
# @Software: PyCharm
import socket
#创建一个套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
sock.bind(('',9099))
#得到发送的信息
data,address = sock.recvfrom(521)
#发送信息到一个地址
sock.sendto('server'.encode(),('127.0.0.1',8001))
#打印信息
print(data.decode(),address)
#关闭套接字
sock.close()