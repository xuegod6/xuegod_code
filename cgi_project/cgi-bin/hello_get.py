# -*- coding: utf-8 -*-
# @Time : 2019/1/17 14:50 
# @Author : for 
# @File : hello_get.py 
# @Software: PyCharm
import cgi,cgitb
#创建实例化
form = cgi.FieldStorage()
#得到前端专递过来的值name，age
site_name = form.getvalue('name')
site_url = form.getvalue('age')
#发送给浏览器！ 告知浏览器我们要显示的内容text/html
print('Content-type:text/html')
print()  # 告诉服务器结束头部信息
#响应的前端数据
print ("<html>")
print ("<head>")
print ("<meta charset='GBK'>")
print ("<title>这不是演习</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s的年龄%s</h2>" % (site_name, site_url))
print ("</body>")
print ("</html>")
