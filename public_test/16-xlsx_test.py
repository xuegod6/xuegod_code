# -*- coding: utf-8 -*-
# @Time : 2018/12/14 15:48 
# @Author : for 
# @File : 16-xlsx_test.py 
# @Software: PyCharm
import xlsxwriter
#创建exc文档
workbook = xlsxwriter.Workbook('./static/demo.xlsx')
#创建工作报表独对象
worksheet = workbook.add_worksheet()
#a-e列设置长度
worksheet.set_column('A:E',20)
#格式化
bold = workbook.add_format({'bold':True})
#再短远哥内写入想要的字符，
worksheet.write('A1','hello')
worksheet.write('A2','word',bold)
worksheet.write('B2','中文测试',bold)

worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.insert_image('B5','1.png')

workbook.close()


