# -*- coding: utf-8 -*-
# @Time : 2018/12/20 15:13 
# @Author : for 
# @File : 10_shizhan_test.py 
# @Software: PyCharm
import pandas as pd
import re

gbp_path = './static/china_gdp.csv'
pop_path = './static/people_num.csv'

gbp_data = pd.read_csv(gbp_path,encoding='GB2312')
pop_data = pd.read_csv(pop_path,encoding='GB2312')

import numpy as np
from pyecharts import Map

attr = gbp_data['地区'].values.tolist()
# print(attr)
# attr =
attr = [re.sub('[自治区市省回族维吾尔壮族]','',i)for i in attr]

v1 = gbp_data['2017年'].values
v2 = pop_data['2017年'].values

value = np.round(v1/v2,decimals=2).tolist()
# print(value)
map = Map('2017人均收入',title_pos='auto',title_color='blue',width=1200,height=600)

map.add('人均/万',attr,value,visual_range=[0,12],maptype='china',is_visualmap=True,visual_text_color='#000')

map.render()
# attr = gbp_data['地区'].values.tolist()
# print(attr)


