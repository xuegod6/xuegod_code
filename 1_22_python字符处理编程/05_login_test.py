# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:42
# @Author  : for 
# @File    : 05_login_test.py
# @Software: PyCharm
import hashlib
#todo：模拟数据库
user = {"name":'bob',"password":'e10adc3949ba59abbe56e057f20f883e'}
#salt
class User_login(object):
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        md5 = hashlib.md5()
        md5.update(self.password.encode())
        password = md5.hexdigest()
        if self.name ==user['name'] and user['password'] == password:
            print('密码正确')
            return ''
        else:
            print('账号密码不正确')
            return ''

if __name__ == '__main__':
    name = input('请输入姓名：')
    password = input('请输入密码:')
    user_login = User_login(name,password)
    user_login.login()