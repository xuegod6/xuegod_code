# -*- coding: utf-8 -*-
# # @Time : 2018/12/11 15:21
# # @Author : for
# # @File : 08-dec_test.py
# # @Software: PyCharm
import time
a = ['while','for','django']
def outer(func):
    def a(name):
        func(name)
        print('开始判断你有没有登录？')
        time.sleep(2)
        if name in a:
            print('你已经登录成功了，请访问')
            time.sleep(1)
        else:
            print('你没有登录，没有访问权限')
    return a
@outer('fasds') # login = outer(login)
def login(name):
    print('我要浏览')
login('for')