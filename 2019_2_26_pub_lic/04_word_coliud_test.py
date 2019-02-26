# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 11:13
# @Author  : for 
# @File    : 04_word_coliud_test.py
# @Software: PyCharm
import jieba
from wordcloud import WordCloud,STOPWORDS
wc = WordCloud(
    background_color='white',
    max_words=2000,
    max_font_size=100,
    stopwords=STOPWORDS.add('国'),
    font_path='C:\Windows\Fonts\simfang.ttf',
    random_state=42

)
text = open('poem.txt',encoding='utf-8').read()

def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts,cut_all=False)
    for word in word_generator:
        words_list.append(word)
    # print(words_list)
    return ' '.join(words_list)
text = stop_words(text)
wc.generate(text)
wc.to_file('2.png')