# -*- coding: utf-8 -*-
# @Time : 2018/12/21 10:31 
# @Author : for 
# @File : hello_get.py 
# @Software: PyCharm
import cgi,cgitb
#创建实例化
form = cgi.FieldStorage()

site_name = form.getvalue('name')
site_url = form.getvalue('age')

print("Content-type:text/html")
print()
print ("<html>")
print ("<head>")
print ("<meta charset=GBK'>")
print ("<title>这不是演习</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s的年龄%s</h2>" % (site_name, site_url))
print ("</body>")
print ("</html>")