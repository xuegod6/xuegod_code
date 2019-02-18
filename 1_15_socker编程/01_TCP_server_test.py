# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 21:08
# @Author  : for 
# @File    : 01_TCP_server_test.py
# @Software: PyCharm
import socket
#创建一个套接字，并且以tcp连接
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定套接字，，参数为元组，如果写空带包本地所有ip
#第二个参数是端口0-65535 2^16 -1
sock.bind(('',9000))
#监听 最大的端口数5
sock.listen(5)
#接受请求
#content 这是信道
#address 请求用户的身份
content,address = sock.accept()

print('%s:%s id connected....'%address)
#发送数据
content.send('hello'.encode())
#接受数据
print(content.recv(521).decode())
#关闭套接字
sock.close()