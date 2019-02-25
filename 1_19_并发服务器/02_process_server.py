# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 21:00
# @Author  : for 
# @File    : 02_process_server.py
# @Software: PyCharm
from socket import *
from multiprocessing import Process
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
    serSocket = socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddr = ('',7788)
    serSocket.bind(localAddr)
    serSocket.listen(5)
    try:
        while True:
            print('----主进程等地啊新的客户端到来---')
            newSocket,destAddr= serSocket.accept()
            print('---主进程接下来处理数据[%s]----'%(str(destAddr)))
            client = Process(target=dealWithClient,args=(newSocket,destAddr))
            client.start()
            #应为已经向子进程中copy了一份医用了，并且父进程中的这个套接字也没有用处了，为了防止占用过多的资源，我们关闭
            newSocket.close()
    finally:
        serSocket.close()
if __name__ == '__main__':
    main()




