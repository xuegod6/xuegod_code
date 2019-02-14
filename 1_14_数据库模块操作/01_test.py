#导入词云
from wordcloud import WordCloud
#打开文件并且读取完全
f = open('china_word.txt','r',encoding='utf-8').read()
#创建wc设个实例对象，里面可传递相应的参数
#generate根据文本生成词云
wc = WordCloud(
    background_color='white',
    width=500,
    font_path="C:/Windows/Fonts/STFANGSO.ttf",
    height=366,
    margin=2
).generate(f)
#to_file 输出到文件
wc.to_file('./image/0.jpg')
