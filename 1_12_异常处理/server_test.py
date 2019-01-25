# -*- coding: utf-8 -*-
# @Time    : 2019/1/25 15:05
# @Author  : for 
# @File    : server_test.py
# @Software: PyCharm
import socket
#创建一个套接字，并且以tcp连接
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定套接字，参数为双元素元组，如果写空代表本地所有ip
#第二个参数是端口 0-65535，就是2^16-1
sock.bind(('',9000))
#监听，最大端口为5
sock.listen(5)
#接收连接请求
#conntent 用来接收请求用户的消息和发送对该用户的的消息功能
#address 是请求用户的身份（ip,port)
content,address = sock.accept()
print('%s:%s id connected……'%address)
#发送数据,encode字符串编码
content.send('hello'.encode())
#接收数据参数是字节的形式,decode()解码
print(content.recv(521).decode())
#关闭套接字
sock.close()
