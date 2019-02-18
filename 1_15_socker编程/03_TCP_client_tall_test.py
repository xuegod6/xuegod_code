# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 21:55
# @Author  : for 
# @File    : 03_TCP_client_tall_test.py
# @Software: PyCharm
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9001))
print('已经建立连接....')
info = ''
while info != 'exit':
    send_mes = input('>>>')
    s.send(send_mes.encode())
    if send_mes == 'exit':
        break
    info = s.recv(1024).decode()
    print('服务器:'+info)
s.close()
