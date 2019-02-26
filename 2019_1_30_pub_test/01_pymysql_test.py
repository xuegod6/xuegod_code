# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 13:37
# @Author  : for 
# @File    : 01_pymysql_test.py
# @Software: PyCharm
import pymysql
#连接数据库，参数分别为本地地址，用户名，密码，数据库，字符集
db = pymysql.connect('localhost','root','123456','new_test',charset='utf8')
#使用cursor方法创建一个游标对象，相当于一个操作者
cursor = db.cursor()
# 使用 execute()  方法执行sql语句
sql = "insert into test_sql(name,age) VALUE (%s,%s)"
while True:
    name = input('请输入你输入的姓名:')
    age = int(input('输入一串数字:'))
    #execute()这行SQL语句
    cursor.execute(sql,[name,age])
    #提交
    db.commit()
#关闭游标
cursor.close()
#关闭数据库
db.close()
