# -*- coding: utf-8 -*-
# @Time : 2019/1/16 15:35 
# @Author : for 
# @File : 04_tcp_client_test.py 
# @Software: PyCharm
from socket import *
import random
import time

serverIp = '127.0.0.1'

s = socket(AF_INET, SOCK_STREAM)
s.connect((serverIp, 7788))
s.send('这是一个测试'.encode())
s.close()

