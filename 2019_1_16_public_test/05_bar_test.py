# -*- coding: utf-8 -*-
# @Time : 2019/1/16 20:40 
# @Author : for 
# @File : 05_bar_test.py 
# @Software: PyCharm

# #创建实例 生成标题
# bar = Bar('我的第一个图表','这里是副标题')
# #图表中添加我们的按钮 种类x 对应的值
# bar.add('服装',['衬衫','羊毛衫','雪猫','裤子','高跟鞋','丝袜'],[5,20,36,10,75,90],is_more_utils=True)
# bar.show_config()
# bar.render()#默认生成一个html render.html
# import random
# v1 = [random.randrange(10,100)for i in range(12)]
# v2 = [random.randrange(10,100)for i in range(12)]
#
# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#
# from pyecharts import Bar
# bar = Bar('这是一个测试','真是一个测试')
# bar.add('商家A',attr,v1,mark_line=['min','average','max'])
# bar.add('商家b',attr,v2,mark_line=['min','average','max'])
# bar.render()
# from pyecharts import Gauge
#
# gauge = Gauge('仪表盘')
# gauge.add('业务指标','完成率',66.66)
# gauge.show_config()
# gauge.render()

from pyecharts import Map
# value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
# attr =["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
#
# map = Map('Map实例',width = 1200,height = 600)
# map.add('',attr,value,maptype='china',is_visualmap=True,visual_text_color='#000')
#
# map.render()

value = [20,190,253,77,65]
attr = ['许昌市', '郑州市', '开封市', '漯河市', '信阳市']
map = Map('河南省实例',width = 1200,height = 600)
map.add('',attr,value,maptype='河南',is_visualmap=True,visual_text_color='#000')
map.render()











