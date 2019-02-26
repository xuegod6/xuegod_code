# -*- coding: utf-8 -*-
# @Time    : 2019/1/28 15:51
# @Author  : for 
# @File    : 03_shizhan_test.py
# @Software: PyCharm
import time
a = ['while','for','django']
def outer(func):
    def inner(name):
        func(name)
        print('开始判断你有没有登录')
        time.sleep(2)
        if name in a:
            print('已经登录成功，请尽情访问')
            time.sleep(1)
        else:
            print('你没有登录，没有权限访问')
            time.sleep(1)
    return inner
@outer
def login(name):
    print('%s 要操作浏览'%name)
@outer
def shopping():
    print('111')

login('fo')