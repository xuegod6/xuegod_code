# -*- coding: utf-8 -*-
# @Time : 2019/1/19 10:44 
# @Author : for 
# @File : 03_xlsx_test.py 
# @Software: PyCharm
# import xlwt
# #创建一个excel实例，创建一个对象方便后期操作
# workbook = xlwt.Workbook(encoding='utf-8')
# #在这个excel文本中我们创建一个表
# sheet = workbook.add_sheet('test')
# #对表进行的写入！写入文本，第一各参数道标的是列坐标，第二个是行，文本内容
# sheet.write(0,0,'name')
# sheet.write(1,0,'project')
# sheet.write(0,1,'while')
# sheet.write(1,1,'for')
# #把刚刚上面所操作的文本保存为一个excel
# workbook.save('xuegod.xls')

import xlwt
#我们创建这个excel实例 方便操作
workbook = xlwt.Workbook(encoding='utf-8')
#在exce中创建工作报表
sheet = workbook.add_sheet('test')
#打开文本 进行写入
with open('cpuinfo') as f:
    #读取一行
    lines = f.readlines()
    #美剧索引，进行遍历
    for index,line in enumerate(lines):
        #对一行内容进行分割数据清洗
        lineSplit = line.split(':')
        #如果你的数据是两个
        if len(lineSplit) == 2:
            #序列解包赋值
            key,value = lineSplit
            #key和value值进行前后去除特殊字符 、\n
            key = key.strip()
            value = value.strip()
            #我们在sheet中写入对用的文本 第一个参数而是列控制，第二个是行控制 第三个是写入的文本内容
            sheet.write(index,0,key)
            sheet.write(index,1,value)
#保存
workbook.save('cpu.xls')













