from wordcloud import WordCloud
#打开文件获取数据
f = open('china_word.txt','r',encoding='utf-8').read()
#创建wc这个对象，里面对应传参
#generate方法生成词云
wc = WordCloud(
    background_color='white',
    width=500,
    height=366,
    margin=2
).generate(f)
#to_file吧词云保存为本地的图片
wc.to_file('./image/0.jpg')