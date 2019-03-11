# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 10:12
# @Author  : for 
# @File    : 01_bea_test.py
# @Software: PyCharm
from bs4 import BeautifulSoup as BS

text = '''
<html>
<head>
    <meta = charset='UTF-8' >
    <title id =1 href = 'http://example.com/elsie' class = 'title'>Test</title>
</head>
<body>
   <div class = 'ok'>
       <div class = 'nice'>
           <p class = 'p'>
               Hello World
           </p>
            <p class = 'e'>
               风一般的男人
           </p>
       </div>
   </div>
</body> 
</html>
'''
import re
soup = BS(text,'lxml')
# name text attrs get
# print(soup.find('p'))
print(soup.find_all(attrs={'class':'e'}))
