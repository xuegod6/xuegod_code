# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 10:17
# @Author  : for 
# @File    : 01_bs_test.py
# @Software: PyCharm
from bs4 import BeautifulSoup as BS

text = '''
<html>
<head>
    <meta  charset='UTF-8' >
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
soup = BS(text,'lxml')
# print(soup.find('body'))
print(soup.find_all(attrs={'class':'e'}))