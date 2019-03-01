# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 22:22
# @Author  : for 
# @File    : 09_server_test.py
# @Software: PyCharm
import socket
import threading
import time
def setResponse(sock,address):
    print('%s:%s is connecte'%(address))
    while True:
        recv = sock.recv(521)
        print(recv)
        sock.send(b'hello %s:%d I am your server'%(address[0].encode(),address[1]))
        time.sleep(1)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',8000))
sock.listen(5)
while True:
    client,address =sock.accept()
    t = threading.Thread(target=setResponse,args=(client,address))
    t.start()
sock.close()
