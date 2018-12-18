# -*- coding: utf-8 -*-
# @Time : 2018/12/14 10:10 
# @Author : for 
# @File : 13-xlsx-test.py 
# @Software: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook('./static/demo.xlsx')

worksheet = workbook.add_worksheet()

worksheet.set_column('A:E',20)

bold = workbook.add_format({'bold':True})

worksheet.write("A1",'hello')
worksheet.write("A2",'word',bold)
worksheet.write("B2",'中文测试',bold)
# worksheet.write("A1",'hello')
worksheet.write(2,0,32)
worksheet.write(3,0,35.5)
worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.insert_image('B5','1.png')

workbook.close()
