# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 21:20
# @Author  : for 
# @File    : 03_thread_socket_test.py
# @Software: PyCharm
from socket import *
from threading import Thread
from time import sleep
def dealWithClient(newSocket,destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if recvData:
            print('recv[%s]:%s'%(str(destAddr),recvData.decode()))
        else:
            print('[%s]客户端已经关闭'%str(destAddr))
            break
    newSocket.close()
def main():
    serSocket =  socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddr = ('',7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)
    try:
        while True:
            print('----主进程等地啊新的客户端到来---')
            newSocket,destAddr= serSocket.accept()
            print('---主进程接下来处理数据[%s]----'%(str(destAddr)))
            client = Thread(target=dealWithClient,args=(newSocket,destAddr))
            client.start()
            #因为线程中共享这个是套接字，如果关闭信道会导致这个套接字不能使用
            #但是此时我们要处理数据，这个套接字还在接受数据，盈测不能关闭
            # newSocket.close()
    finally:

        serSocket.close()
if __name__ == '__main__':
    main()