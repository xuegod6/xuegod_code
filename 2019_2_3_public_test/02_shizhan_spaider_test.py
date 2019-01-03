# -*- coding: utf-8 -*-
# @Time : 2019/1/3 15:46 
# @Author : for 
# @File : 02_shizhan_spaider_test.py 
# @Software: PyCharm
from urllib import request
from lxml import etree
#请求地址
url = 'https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1'
#伪装留恋其
headers={
'Referer': 'https://read.qidian.com/chapter/9r9u8W1evJUCpOPIBxLXdQ2/eSlFKP1Chzg1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
}
#模拟浏览器进行服务器访问
req = request.Request(url=url,headers=headers)
#发起请求
response = request.urlopen(req)
#得到响应文本
content = response.read().decode()
#吧爬取的文本内容编程xpath可匹配的文本
xpath_content = etree.HTML(content)
new_content = xpath_content.xpath('//*[@id="chapter-382639401"]/div/div/p/text()')
# print(new_content)
with open('2.txt','w',encoding='utf-8') as f:
    for i in new_content:
        f.writelines(i.strip())
from wordcloud import WordCloud
from scipy.misc import imread
back_color = imread('1.png')
wc = WordCloud(
    background_color='white',
    max_words=1000,
    mask= back_color,
    font_path='C:\Windows\Fonts\simfang.ttf',
    random_state=42,
)
import jieba
#添加词语操作！ 意思是我是王子就是就想防御一个整词
jieba.add_word('我是王子')
#打开文本
text = open('2.txt',encoding='utf-8').read()
#结巴处理文本结构 达到分词的目的
def stop_words(texts):
    words_list = []
    #结巴分词 生成一个可迭代对象
    word_generator = jieba.cut(texts,cut_all=False)
    with open('stopwords.txt',encoding='utf-8') as f:
        str_text = f.read()
    for word in word_generator:
        #如果结巴粉刺好文本没有还有stopword文本的内容 就添加
        if word.strip() not in str_text:
            #数据添加
            words_list.append(word)
        #数据拼接
    return ' '.join(words_list)
text = stop_words(text)
# print(text)

wc.generate(text)

wc.to_file('./image/7.png')




