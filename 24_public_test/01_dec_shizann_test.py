# -*- coding: utf-8 -*-
# @Time : 2018/12/24 15:20 
# @Author : for 
# @File : 01_dec_shizann_test.py 
# @Software: PyCharm
import time

a = ['while','for','django']

def outer(func):
    def inner(name):
        func(name)
        print('开始判断有没有登录权限')
        time.sleep(2)
        if name in a:
            print('已经登录成功，有权限')
            time.sleep(2)
        else:
            print('你没有登录，么有权限访问')
            time.sleep(2)
    return inner

@outer
def login(name):
    print('%s要浏览'%name)
login('for')