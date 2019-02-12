# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 17:12
# @Author  : for 
# @File    : test.py
# @Software: PyCharm
#coding = utf-8
#coding = utf-8
#coding=utf-8
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9002))
print('wait ....')
while True:
    data,addr = s.recvfrom(1024)
    print('客户端：'+data.decode())
    info = input('>>>')
    if data.decode() == 'exit':
        break
    s.sendto(info.encode(),addr)
s.close()





