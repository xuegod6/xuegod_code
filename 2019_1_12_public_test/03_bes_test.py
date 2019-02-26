# -*- coding: utf-8 -*-
# @Time : 2019/1/12 10:13 
# @Author : for 
# @File : 03_bes_test.py 
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
soup = BS(text,'lxml')

# print(soup.find('p'))
# print(soup.find_all('p'))
import re
# print(soup.find_all(re.compile('^p')))
# print(soup.find_all('p',class_ = 'p'))
# print(soup.find_all(attrs={'class':'e'}))

# print(soup.title)#获取标签
# print(soup.title.name)#获取当前标签中的name
# print(soup.title.text)#获取当前标签中的文本
# print(soup.title.attrs)#获取当前标签中的属性
# print(soup.title.get('class'))#获取当前标签中的摸一个属性
# print(soup.prettify())
# print(type(soup.prettify()))
# print(soup)
# print(type(soup))
# print(soup.title.string)#获取当前标签中的内容
# print(soup.p.string)#获取第一个标签中的内容