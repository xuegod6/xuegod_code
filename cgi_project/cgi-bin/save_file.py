# -*- coding: utf-8 -*-
# @Time : 2018/12/22 21:11 
# @Author : for 
# @File : save_file.py 
# @Software: PyCharm
import cgi,os
#创建实力
form = cgi.FieldStorage()
#得到实力当中的filename
fileitem = form['filename']
#如果有filename
if fileitem.filename:
    try:
        #利用os进行拼接路径name
        fn = os.path.basename(fileitem.filename)
        #打开保存
        open(fn,'wb').write(fileitem.file.read())

    except:
        message = fn + '文件没有上传'
    else:
        message = fn + '文件已经上传'
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
