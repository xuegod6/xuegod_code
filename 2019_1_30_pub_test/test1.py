# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 17:22
# @Author  : for 
# @File    : test1.py
# @Software: PyCharm
#coding=utf-8
import socketserver
#创建一个类，继承BaseRwequsetHanler
class MYHandle(socketserver.BaseRequestHandler):
    #类似于构造函数__init__
    def setup(self):
        print('myhandle is start ')
    #用来处理逻辑
    def handle(self):
        #self.server 当前服务
        #self.client_address 客户端的身份（ip.port
        #self.request 用来接收和发送数据
        print(self.server)
        print('%s:%s is connect '%self.client_address)
        recv = self.request.recv(521)
        print(recv)
        self.request.send('i am server '.encode())
    #类似于析构函数__del__
    def finish(self):
        print('myhandle is stop ')
if __name__ == '__main__':
    #第一个参数来绑定ip
    #第二个位开启对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),MYHandle)
    #开启服务，永远开启
    server.serve_forever()

# 客户端代码（客户端还是使用socket）
#coding=utf-8
import socket
#创建一个sock对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接IP地址
sock.connect(('127.0.0.1',8000))
#发送信息
sock.send('client2'.encode())
#接收信息
print(sock.recv(521).decode())
#关闭套接字
sock.close()
