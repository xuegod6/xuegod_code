# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 22:03
# @Author  : for 
# @File    : 04_UDP_server_tall_test.py
# @Software: PyCharm
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9002))
print('wait...')
while True:
    data,addr = s.recvfrom(1024)
    print('客户端:'+data.decode(),addr)
    info = input('>>>')
    if data.decode() == 'exit':
        break
    s.sendto(info.encode(),addr)
s.close()