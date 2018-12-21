# -*- coding: utf-8 -*-
# @Time : 2018/12/21 10:49 
# @Author : for 
# @File : save_file.py 
# @Software: PyCharm
import cgi,os
import cgitb;cgitb.enable()
form = cgi.FieldStorage()
fileitem = form['filename']
if fileitem.filename:
    try:
        fn =  os.path.basename(fileitem.filename)
        open(fn,'wb').write(fileitem.file.read())
    except :
        message = fn + '文件没有上传'
    else:
        message = fn+'文件上传'
else:
    message = '文件没有上传'
print ("""\
Content-Type: text/html\n
<html>
<head>
<meta charset="GBK">
<title>文件上传</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message))