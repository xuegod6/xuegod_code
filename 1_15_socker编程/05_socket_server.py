# -*- coding: utf-8 -*-
# @Time    : 2019/2/16 22:20
# @Author  : for 
# @File    : 05_socket_server.py
# @Software: PyCharm
import socketserver
class MYHandle(socketserver.BaseRequestHandler):
    #相当于init
    def setup(self):
        print('myhandle is start ')
    #用户交互，数据交互（'127.0.0.1,9001)
    def handle(self):
        print(self.server)
        print('%s:%s is connented'%self.client_address)
        recv = self.request.recv(521)
        print(recv.decode())
        self.request.send(' I am server'.encode())
    #相当于 del
    # def f
    def finish(self):
        print('muhanle is stop')
if __name__ == '__main__':
    #开启线程来处理不同客户端
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8000),MYHandle)
    #开启服务，永远监听
    server.serve_forever()
