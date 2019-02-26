# -*- coding: utf-8 -*-
# @Time : 2019/1/17 15:13 
# @Author : for 
# @File : save_file.py 
# @Software: PyCharm
import cgi,os
import cgitb;cgitb.enable()
form = cgi.FieldStorage()

fileitem = form['filename']

if fileitem.filename:
    try:
        fn = os.path.basename(fileitem.filename)
        open(fn,'wb').write(fileitem.file.read())
    except:
        message = fn + '文件没有上传'
    else:
        message = fn + '文件已经上传'
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
