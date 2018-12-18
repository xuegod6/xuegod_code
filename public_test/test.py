'''from pyecharts import Bar, Line
from pyecharts.engine import create_default_environment

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

line = Line("我的第一个图表", "这里是副标题")
line.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])

env = create_default_environment("html")
# 为渲染创建一个默认配置环境
# create_default_environment(filet_ype)
# file_type: 'html', 'svg', 'png', 'jpeg', 'gif' or 'pdf'

env.render_chart_to_file(bar, path='bar.html')
env.render_chart_to_file(line, path='line.html')
import sys
# from imp import reload
# reload(sys)
# sy('utf-8')'''
import pandas as pd
from pyecharts import Bar
gdp_path='provinces_gdp.csv'  #各省GDP文件路径
pop_path='provinces_population.csv'  #各省人口文件路径
gdp_data = pd.read_csv(gdp_path,encoding='GB2312')  #pandas读入csv表格
pop_data = pd.read_csv(pop_path,encoding='GB2312')

attr = gdp_data['地区'].values.tolist()

v1=gdp_data['2016年'].values.tolist() #2016年各省GDP
v2=pop_data['2016年'].values.tolist() #2016年各省人口
bar = Bar("2016年各省GDP人口条形图",title_color="#fff", title_pos="auto",
      width=1200, height=600,background_color="white")
bar.add("GDP/亿元", attr, v1)
bar.add("人口/万", attr, v2, is_label_show=True,is_datazoom_show=True,
        xaxis_label_textsize=10,xaxis_rotate=30)
bar.render('./static/1.html')


