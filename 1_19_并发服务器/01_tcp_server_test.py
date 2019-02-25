# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 20:34
# @Author  : for 
# @File    : 01_tcp_server_test.py
# @Software: PyCharm
from socket import *
serSocket = socket(AF_INET,SOCK_STREAM)
#设置柯崇敷使用的绑定信息
serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
localAddr = ('',7788)
serSocket.bind(localAddr)
serSocket.listen(5)
while True:
    print('----主进程等待客户端的到来---')
    newSocket,destAddr = serSocket.accept()
    print('----主进程接下来赋值处理[%s]---'%str(destAddr))
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
serSocket.close()


