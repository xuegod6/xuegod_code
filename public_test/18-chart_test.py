# -*- coding: utf-8 -*-
# @Time : 2018/12/14 16:46 
# @Author : for 
# @File : 18-chart_test.py 
# @Software: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook('./static/demo.xlsx')

worksheet = workbook.add_worksheet()

data = [
[150,152,158,149,155,145,148],
[89, 88,95,93, 98,100, 99],
[201,200,198,175,170,198,195],
]
worksheet.write_row('A1',data[0])
worksheet.write_row('A2',data[1])
worksheet.write_row('A3',data[2])

chart = workbook.add_chart({'type':'column'})


chart.add_series({
        'categories':'=Sheet1!$A$1:$G$1',
        'values': '=Sheet1!$A$1:$G$1',
        'line': {'color':'black'},
})

chart.set_x_axis({
    'name': 'Earnings per Quarter',             # 设置 X 轴标题名称
    'name_font':{ 'size':14,'bold':True},  # 设置 X 轴标题字体属性
    'num_font' :{ 'italic': True },                # 设置 X 轴数字字体属性
})

chart.set_size({ 'width':577,'height':287})    # 设置图表大小
chart.set_title({'name':u'业务流量周报图表'})  #设置图表(上方)大标题
chart.set_y_axis({'name':'Mb/s'})

worksheet.insert_chart('A4',chart)

workbook.close()









