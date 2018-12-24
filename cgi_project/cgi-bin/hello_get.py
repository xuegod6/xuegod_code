# -*- coding: utf-8 -*-
# @Time : 2018/12/22 20:45 
# @Author : for 
# @File : hello_get.py
# @Software: PyCharm
import cgi
#创建实力化
form = cgi.FieldStorage()
#获取数据
site_name = form.getvalue('name')
site_age = form.getvalue('age')
#这一行发送给浏览器，告知它 显示的内容是text/htnl
print("Content-type:text/html")
print()#告诉服务器 结束头部信息
#展示在前端的html
print ("<html>")
print ("<head>")
print ("<meta charset=GBK'>")
print ("<title>这不是演习</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s的年龄%s</h2>" % (site_name, site_age))
print ("</body>")
print ("</html>")
