# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:55
# @Author  : for 
# @File    : 06_sqlt_test.py
# @Software: PyCharm
import hashlib
#todo：模拟数据库  password:123456salt
user = {"name":'bob',"password":'207acd61a3c1bd506d7e9a4535359f8a'}
#salt
class User_login(object):
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def salt_md5(self,password):
        return password+'salt'
    def login(self):
        md5 = hashlib.md5()
        md5.update(self.salt_md5(self.password).encode())
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