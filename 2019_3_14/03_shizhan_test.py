# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 21:08
# @Author  : for 
# @File    : 03_shizhan_test.py
# @Software: PyCharm
import time,jieba
from urllib import request
from lxml import etree

url ='https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1'

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
#todo:构建请求
req = request.Request(url = url,headers=headers)
#todo:给服务器发送请求
response = request.urlopen(req)
content = response.read().decode()

xpath_content = etree.HTML(content)

new_content = xpath_content.xpath('//*[@id="chapter-382639401"]/div/div/p/text()')

with open('3.txt','w',encoding='utf-8') as f:
    for i in new_content:
        f.writelines(i.strip())

from scipy.misc import  imread
from wordcloud import WordCloud
back_color = imread('1.png')
wc = WordCloud(
    background_color='white',
    max_words=100,
    mask=back_color,
    max_font_size=100,
    font_path='C:\Windows\Fonts\simfang.ttf',
    random_state=42,
)
text = open('2.txt',encoding='utf-8').read()

def stop_word(texts):
    words_list = []
    word_generator = jieba.cut(texts,cut_all=False)
    for word in word_generator:
        words_list.append(word)
    return ' '.join(words_list)

text = stop_word(text)
wc.generate(text)
wc.to_file('test.png')
