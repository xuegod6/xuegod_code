# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 10:33
# @Author  : for 
# @File    : 02_word_cloud_test'.py
# @Software: PyCharm
from wordcloud import WordCloud

f = open('1.txt','r').read()

wc = WordCloud(
    background_color='white',
    width= 500,
    height=366,
    margin=2
).generate(f)

wc.to_file('0.jpg')