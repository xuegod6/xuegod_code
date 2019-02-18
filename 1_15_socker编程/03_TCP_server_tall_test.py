# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 21:48
# @Author  : for 
# @File    : 03_TCP_server_tall_test.py
# @Software: PyCharm
import socket
print('正在连接中....')
def dealclient(sock,addr):
    info = sock.recv(1024).decode()
    while info != 'exit':
        print('客户端:'+info)
        send_mes = input('>>>')
        sock.send(send_mes.encode())
        if send_mes == 'exit':
            break
        info = sock.recv(1024).decode()
    sock.close()
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('127.0.0.1',9001))
    s.listen(1)
    sock,addr = s.accept()
    dealclient(sock,addr)


