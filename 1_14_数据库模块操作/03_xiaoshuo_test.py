# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 15:10
# @Author  : for 
# @File    : 03_xiaoshuo_test.py
# @Software: PyCharm
# 第一步：爬取网站
# 第二步：得到文本内容
# 第三步：利用结巴分词
# 第四步：生成词云
from urllib import request
from lxml import  etree
url = 'https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1'

#请求的头部
headers = {
    "Referer": "https://read.qidian.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
req = request.Request(url = url,headers = headers)
response = request.urlopen(req)
content = response.read().decode()
xpath_content = etree.HTML(content)
new_content = xpath_content.xpath('//*[@id="chapter-382639401"]/div/div/p/text()')
with open('2.txt','w',encoding='utf-8') as f:
    for i in new_content:
        f.writelines(i.strip())

from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS
import time

time.sleep(2)

back_color = imread('1.png')

wc = WordCloud(
    background_color='white',
    max_words=1000,
    mask= back_color,
    max_font_size=100,
    stopwords=STOPWORDS.add('的'),
    font_path='C:\Windows\Fonts\simfang.ttf',
    random_state=42,
)
text = open('2.txt',encoding='utf-8').read()
import jieba
jieba.add_word('我是王')
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts,cut_all=False)
    for word in word_generator:
        words_list.append(word)
    print(words_list)
    return ' '.join(words_list)

text = stop_words(text)
wc.generate(text)
wc.to_file('./image/test.jpg')
