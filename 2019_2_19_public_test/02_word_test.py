# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 10:40
# @Author  : for 
# @File    : 02_word_test.py
# @Software: PyCharm
import jieba
from wordcloud import WordCloud,STOPWORDS
wc = WordCloud(background_color='white',  # 背景颜色
               max_words=1000,  # 最大词数
               # mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
               max_font_size=100,  # 显示字体的最大值
               stopwords=STOPWORDS.add('国'),  # 使用内置的屏蔽词，再添加'苟利国'
               # font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
               font_path='C:\Windows\Fonts\simfang.ttf',
               random_state=42,  # 为每个词返回一个PIL颜色
               # width=1000,  # 图片的宽
               # height=860  #图片的长
               )
text = open('poem.txt').read()
# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    for word in word_generator:
        words_list.append(word)
    print(words_list)
    return ' '.join(words_list)  # 注意是空格
text = stop_words(text)
wc.generate(text)
# 显示图片
wc.to_file('maikou.png')
