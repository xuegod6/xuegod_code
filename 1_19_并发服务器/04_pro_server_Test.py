# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 21:43
# @Author  : for 
# @File    : 04_pro_server_Test.py
# @Software: PyCharm
from socket import *
import time
#存储一个新的socket信息
g_socketList = []
def main():
    serSocket =  socket(AF_INET,SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddr = ('',7788)
    serSocket.bind(localAddr)
    serSocket.listen(2)
    #讲套接字设置成非阻塞
    #试着为非阻塞之后如何accept时候，没有客户端connect ，那么会出现一个异常!
    #需要一个try来进行处理
    serSocket.setblocking(False)
    while True:
        try:
            newClientInfo = serSocket.accept()
        except Exception as e:
            pass
        else:
            print('一个新的客户端到来：%s'%str(newClientInfo))
            newClientInfo[0].setblocking(False)
            g_socketList.append(newClientInfo)
            #用来存储需要删除的客户端信息
        needDelClientInfoList = []
        for clientSocket,clientAddr in g_socketList:
            try:
                recvData = clientSocket.recv(1024)
                if recvData:
                    print('recv[%s]:%s'%(str(clientAddr),recvData.decode()))
                else:
                    print('[%s]客户端已经关闭'%str(clientAddr))
                    clientSocket.close()
                    needDelClientInfoList.append((clientSocket,clientAddr))
            except Exception as e:
                pass
        for needDelClientInfo in needDelClientInfoList:
            g_socketList.remove(needDelClientInfo)
if __name__ == '__main__':
    main()

