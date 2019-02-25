# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 22:15
# @Author  : for 
# @File    : 05_selet_server.py
# @Software: PyCharm
from socket import *
from select import select
import sys
def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    localAddr = ('127.0.0.1', 7788)
    serSocket.bind(localAddr)
    #设置服务器为非阻塞式！
    serSocket.setblocking(False)
    serSocket.listen(100)
    inputs = [serSocket]
    running = True
    while True:
        readable, writable, exceptionable = select(inputs, [], [])
        for sock in readable:
            if sock == serSocket:
                clientSocket, clientAddr = serSocket.accept()
                print('newClient[%s]'%str(clientAddr))
                inputs.append(clientSocket)
            elif sock == sys.stdin:
                cmd = sys.stdin.readline()
                running = False
                break
            else:
                massage = sock.recv(1024)
                if massage:
                    print('massage from [%s] is %s'%(str(clientAddr), massage.decode('utf-8')))
                else:
                    print('[%s] was closed'%(str(clientAddr)))
                    inputs.remove(sock)
                    sock.close()
        if not running:
            break
    serSocket.close()
if __name__ == '__main__':
    main()
