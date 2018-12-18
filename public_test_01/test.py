# -*- coding: utf-8 -*-
# @Time : 2018/12/17 9:28 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
'''
from pyecharts import Bar
#bar 就是柱状图
bar = Bar("我的第一个图表", '我是副标题')
#添加图表的配置项
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90],is_more_utils=True)
#打印所有的配置项
bar.show_config()
#在前端答疑所有的配置项
bar.get_options()
#自动生成一个html文件 默认的‘index.html
bar.render()
'''
# import random
# v1 = [random.randrange(1,100)for i in range(12)]
# v2 = [random.randrange(1,100)for i in range(12)]
#
# print(v1,v2)
# for i in enumerate('abcder',1):
#     print(i)
#


# from pyecharts import Bar
# v1 = [1.1, 4.9, 7.0, 23.2, 25.6, 76.7, 120.6, 162.2, 32.6, 20.0, 6.4, 3.3]  # 初始化第一组要展示的数据
# v2 = [5.8, 5.9, 9.0, 26.4, 28.7, 100.7, 195.6, 182.2, 48.7, 18.8, 6.0, 5.7]  # 初始化第二组要展示的数据
# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # 指定X轴刻度名字
# bar =Bar("x 轴和 y 轴交换","副标题:展示每一维度数据的最小，最大，平均值")
# bar.add("商家A", attr, v1,mark_line=["min","average", "max"])
# bar.add("商家B", attr, v2, mark_line=["min","average", "max"],is_convert=True)
# bar.render()



# from pyecharts import Bar, Scatter3D
# from pyecharts import Page
# page = Page()         # step 1
# # bar
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [5, 20, 36, 10, 75, 90]
# v2 = [10, 25, 8, 60, 20, 80]
# bar = Bar("柱状图数据堆叠示例")
# bar.add("商家A", attr, v1, is_stack=True)
# bar.add("商家B", attr, v2, is_stack=True)
# page.add(bar)         # step 2
# page.render()
# from pyecharts import Bar
# #attr = ["{}month".format(i) for i in range(1, 13)]  # 指定X轴刻度名字
# attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # 指定X轴刻度名字
# v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]  # 初始化第一组要展示的数据
# v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]  # 初始化第二组要展示的数据
# v3 = [4.0, 6.9, 9.0, 26.2, 28.6, 75.7, 139.6, 168.2, 28.6, 35.0, 2.4, 5.3]  # 初始化第er组要展示的数据
# bar = Bar("Bar chart", "precipitation and evaporation one year")  # 设置图标的名字和标题
# bar.add("precipitation", attr, v1, mark_line=["average"], mark_point=["max", "min"])   # 设置第一组要展示数据的方面(原始护甲，平均值，最大值和最小值)设定图例
# bar.add("evaporation", attr, v2, mark_line=["average"], mark_point=["max", "min"])     # 设置第二组
# bar.add("test_add_more", attr, v3, mark_line=["average"], mark_point=["max", "min"])    # 设置第三组
# bar.render()


# from pyecharts import Scatter
# v1 =[10, 20, 30, 40, 50, 60]
# v2 =[10, 20, 30, 40, 50, 60]
# scatter =Scatter("散点图示例")
# scatter.add("A", v1, v2)
# scatter.add("B", v1[::-1], v2)
# scatter.show_config()
# scatter.render()


# from pyecharts import EffectScatter
# v1 =[10, 20, 30, 40, 50, 60]
# v2 =[25, 20, 15, 10, 60, 33]
# es =EffectScatter("动态散点图示例")
# es.add("effectScatter", v1, v2)
# es.render()



# from pyecharts import EffectScatter
# es =EffectScatter("", "动态散点图各种图形示例")
# es.add("pin_sample", [20], [20], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
# es.add("rect_sample", [30], [30], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
# es.add("roundRect_sample", [40], [40], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
# es.add("diamond_sample", [50], [50], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
# es.add("arrow_sample", [60], [60], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
# es.add("triangle_sample", [70], [70], symbol_size=6, effect_scale=4.5, effect_period=3,symbol="triangle")
# es.show_config()
# es.render()






# from pyecharts import Funnel
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# value =[20, 40, 60, 80, 100, 120]
# funnel =Funnel("漏斗图示例")
# funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
# funnel.render()


# from pyecharts import Gauge
# gauge =Gauge("仪表盘示例")
# gauge.add("业务指标", "完成率", 66.66)
# gauge.show_config()
# gauge.render()


# from pyecharts import Geo
# data =[(u"北京", 9), (u"鄂尔多斯", 12), (u"招远", 12), (u"舟山", 12), (u"齐齐哈尔", 14), (u"盐城", 15)]
# geo =Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
# attr, value =geo.cast(data)
# geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
# geo.render()

# from pyecharts import Graph
# nodes =[{"name": "结点1", "symbolSize": 10}, {"name": "结点2", "symbolSize": 20}, {"name": "结点3", "symbolSize": 30},
#         {"name": "结点4", "symbolSize": 40}, {"name": "结点5", "symbolSize": 10}, {"name": "结点6", "symbolSize": 40},
#         {"name": "结点7", "symbolSize": 30}, {"name": "结点8", "symbolSize": 20}]
# links =[]
# p=0
# for i in nodes:
#     if (p % 2 == 1):
#         continue
#     p += 1
#     for j in nodes:
#
#         links.append({"source": i.get('name'), "target": j.get('name')})
# graph = Graph("关系图-环形布局示例")
# graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
# graph.show_config()
# graph.render()
# from pyecharts import Line
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[5, 20, 36, 10, 10, 100]
# v2 =[55, 60, 16, 20, 15, 80]
# line =Line("折线图示例")
# line.add("商家A", attr, v1, mark_point=["average"])
# line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
# line.show_config()
# line.render()
# line =Line("折线图-阶梯图示例")
# line.add("商家A", attr, v1, is_step=True, is_label_show=True)
# line.show_config()
# line.render()

# from pyecharts import Line
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[5, 20, 36, 10, 10, 100]
# v2 =[55, 60, 16, 20, 15, 80]
# line =Line("折线图-面积图示例")
# line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
# line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
# line.show_config()
# line.render()


# from pyecharts import Liquid
# liquid =Liquid("水球图示例")
# liquid.add("Liquid", [0.6])
# liquid.show_config()
# liquid.render()
# from pyecharts import Liquid
# liquid =Liquid("水球图示例")
# liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
# liquid.show_config()
# liquid.render()


# from pyecharts import Map
# value =[20, 190, 253, 77, 65]
# attr =['许昌市', '郑州市', '开封市', '漯河市', '信阳市市']
# map=Map("河南地图示例", width=1200, height=600)
# map.add("", attr, value, maptype=u'河南', is_visualmap=True, visual_text_color='#000')
# map.show_config()
# map.render()
# from pyecharts import Parallel
# c_schema =[ {"dim": 0, "name": "data"}, {"dim": 1, "name": "AQI"}, {"dim": 2, "name": "PM2.5"}, {"dim": 3, "name": "PM10"}, {"dim": 4, "name": "CO"}, {"dim": 5, "name": "NO2"}, {"dim": 6, "name": "CO2"}, {"dim": 7, "name": "等级", "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}]
# data =[ [1, 91, 45, 125, 0.82, 34, 23, "良"], [2, 65, 27, 78, 0.86, 45, 29, "良"], [3, 83, 60, 84, 1.09, 73, 27, "良"],
#         [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
#         [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"], [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
#         [8, 89, 65, 78, 0.86, 51, 26, "良"], [9, 53, 33, 47, 0.64, 50, 17, "良"], [10, 80, 55, 80, 1.01, 75, 24, "良"],
#         [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"], [12, 99, 71, 142, 1.1, 62, 42, "良"], [13, 95, 69, 130, 1.28, 74, 50, "良"],
#         [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]]
# parallel =Parallel("平行坐标系-用户自定义指示器")
# parallel.config(c_schema=c_schema)
# parallel.add("parallel", data)
# parallel.show_config()
# parallel.render()

#
# # encoding: utf-8
# # 3D 散点图示例
# # scatter3D
# import random
# from pyecharts import Bar, Scatter3D
# from pyecharts import Page
# page = Page()         # step 1
# data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
# range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
#                '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
# scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
# scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
# page.add(scatter3D)  # step 2
# page.render()


# from pyecharts import Pie
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[11, 12, 13, 10, 10, 10]
# v2 =[19, 21, 32, 20, 20, 33]
# pie =Pie("饼图-玫瑰图示例", title_pos='center', width=900)
# pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
# pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area', is_legend_show=False, is_label_show=True)
# pie.show_config()
# pie.render()

# from pyecharts import Polar
# radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
# polar.show_config()
# polar.render()

# from pyecharts import Polar
# radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
# polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
# polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
# polar.show_config()
# polar.render()

# from pyecharts import Radar
# schema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
# v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
# v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
# radar =Radar()
# radar.config(schema)
# radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
# radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
# radar.show_config()


# radar.render()



# from pyecharts import Radar
# value_bj =[ [55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2], [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4]]
# value_sh =[ [91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2], [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4]]
# c_schema=[{"name": "AQI", "max": 300, "min": 5}, {"name": "PM2.5", "max": 250, "min": 20},
#           {"name": "PM10", "max": 300, "min": 5}, {"name": "CO", "max": 5}, {"name": "NO2", "max": 200},
#           {"name": "SO2", "max": 100}]
# radar =Radar()
# radar.config(c_schema=c_schema, shape='circle')
# radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
# radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
# radar.show_config()
# radar.render()

#WordCloud（词云图）
# from pyecharts import WordCloud
# name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A',
#                 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton',
#                 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament',
#                 'Point Break']
# value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
# wordcloud =WordCloud(width=1300, height=620)
# wordcloud.add("词云名字", name, value, word_size_range=[20, 100])
# wordcloud.show_config()
# wordcloud.render()


#
# from pyecharts import WordCloud
# name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A',
#                 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton',
#                 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament',
#                 'Point Break']
# value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
# wordcloud =WordCloud(width=1300, height=620)
# wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
# wordcloud.show_config()
# wordcloud.render()


# 折线图示例
# from pyecharts import Line
# attr =['周一', '周二', '周三', '周四', '周五', '周六', '周日',]
# line =Line("折线图示例")
# line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
# line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"], mark_line=["average"], yaxis_formatter="°C")
# line.show_config()
# line.render()


# from pyecharts import Pie
# pie =Pie("饼图示例", title_pos='center', width=1000, height=600)
# pie.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148], radius=[40, 55],is_label_show=True)
# pie.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30], legend_orient='vertical', legend_pos='left')
# pie.show_config()
# pie.render()


# import random
# from pyecharts import Pie
# attr =['A', 'B', 'C', 'D', 'E', 'F']
# pie =Pie("饼图示例", width=1000, height=600)
# pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[25, 50],is_random=True)
# pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[25, 50],rosetype='area')
# pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[65, 50],is_random=True)
# pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[65, 50],rosetype='radius')
# pie.show_config()
# pie.render()


# from pyecharts import Pie
# pie =Pie('各类电影中"好片"所占的比例', "数据来着豆瓣", title_pos='center')
# pie.add("", ["剧情", ""], [25, 75], center=[10, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, )
# pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, legend_pos='left')
# pie.add("", ["爱情", ""], [14, 86], center=[50, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["冒险", ""], [27, 73], center=[90, 30], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["动作", ""], [15, 85], center=[10, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["喜剧", ""], [54, 46], center=[30, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["科幻", ""], [26, 74], center=[50, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["悬疑", ""], [25, 75], center=[70, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None)
# pie.add("", ["犯罪", ""], [28, 72], center=[90, 70], radius=[18, 24], label_pos='center', is_label_show=True, label_text_color=None, is_legend_show=True, legend_top="center")
# pie.show_config()
# pie.render()
