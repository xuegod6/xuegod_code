# -*- coding: utf-8 -*-
# @Time : 2019/1/16 21:14 
# @Author : for 
# @File : 06_shizhn_test.py 
# @Software: PyCharm
import re
import pandas as pd
import numpy as np
gdp_path = './static/china_gdp.csv'
pop_path = './static/people_num.csv'
gdp_data = pd.read_csv(gdp_path,encoding='GB2312')
pop_data = pd.read_csv(pop_path,encoding='GB2312')
attr = gdp_data['地区'].values.tolist()
print(attr)

v1 = gdp_data['2017年'].values
v2 = pop_data['2017年'].values
# print(v1,v2)
from pyecharts import Map
attr = [re.sub('[自治区市省维吾尔回壮族]','',i)for i in attr]

value = np.round(v1/v2,decimals=2).tolist()
map = Map('2017年全国各省人居收入情况',title_color='#000',title_pos='auto')
map.add('人均收入\万元',attr,value,visual_range=[0,12],maptype='china',is_visualmap=True,visual_text_color='#000')
map.render('全中国收入情况.html')

# print(value)
# print(attr)
