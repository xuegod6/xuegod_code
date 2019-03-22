# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 20:12
# @Author  : for 
# @File    : test01.py
# @Software: PyCharm
import socket

s=socket.socket()

host=socket.gethostname()
port=3456
s.connect((host,port))

cmd=input(">>>")
s.sendall(cmd.encode())
data=s.recv(1024)
print(data.decode())

s.close()
