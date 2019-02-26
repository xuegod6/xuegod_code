# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 14:53
# @Author  : for 
# @File    : 01_tcp_server.py
# @Software: PyCharm
from socket import *
ser_socket = socket(AF_INET,SOCK_STREAM)

ser_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

localAddr = ('',7788)

ser_socket.bind(localAddr)
ser_socket.listen(5)

while True:
    print('----主进程等待新客户端的到来----')
    newSocket,destAddr = ser_socket.accept()
    print('----主进程接下来负责处理[%s]----'%str(destAddr))
    try:
        while True:
            recv_data = newSocket.recv(1024)
            if recv_data:
                print('recv:',recv_data.decode())
            else:
                print('[%s]客户端已经关闭'%str(destAddr))
                break
    except Exception as e:
        print(e)
    finally:
        newSocket.close()
