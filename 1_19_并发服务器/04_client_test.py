# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 21:53
# @Author  : for 
# @File    : 04_client_test.py
# @Software: PyCharm
from socket import  *
import  random
import time
serverIp = input('请输入服务器的IP：')
connNum = input('请输入连接服务器的次数（例如1000）')
g_socketList = []
for i in range(int(connNum)):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((serverIp,7788))
    g_socketList.append(s)
    print(i)
while True:
    for s in g_socketList:
        s.send(b'client')
