# -*- coding: utf-8 -*-
# @Time : 2019/1/3 13:54 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
import jieba
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from urllib import request
import time
from lxml import etree
#定义请求的地址
url = "https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1"
#请求的头部
headers = {
    "Referer": "https://www.qiushibaike.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
#构建请求
req = request.Request(url = url,headers = headers)
#发起请求
response = request.urlopen(req)
#接收返回的内容，返回的内容以类文件的形式返回
content = response.read().decode()
xpath_content =  etree.HTML(content)
new_content = xpath_content.xpath('//*[@id="chapter-382639401"]/div/div/p/text()')
with open('2.txt','w',encoding='utf-8') as f:
    for i in new_content:
        f.writelines(i.strip())
time.sleep(2)

back_color = imread('1.png')  # 解析该图片

wc = WordCloud(background_color='white',  # 背景颜色
               max_words=1000,  # 最大词数
               mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               stopwords=STOPWORDS.add('国'),  # 使用内置的屏蔽词，再添加'苟利国'
               # font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               font_path='C:\Windows\Fonts\simfang.ttf',
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )
# WordCloud各含义参数请点击 wordcloud参数

# 添加自己的词库分词，比如添加'我是王'到jieba词库后，当你处理的文本中含有我是王这个词的时候自动把他认为一个词语
jieba.add_word('我是王')

# 打开词源的文本文件
text = open('2.txt',encoding='utf-8').read()

# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    # print('textssss',list(word_generator))
    #在这里已经要注意stopword中的分词要一词一行
    with open('stopwords.txt',encoding='utf-8') as f:
        str_text = f.read()
        unicode_text = str_text # 把str格式转成unicode格式
    for word in word_generator:
        if word.strip() not in str_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格
text = stop_words(text)

print(text)

wc.generate(text)

wc.to_file('./image/2.png')


