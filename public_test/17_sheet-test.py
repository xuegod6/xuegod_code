# -*- coding: utf-8 -*-
# @Time : 2018/12/14 16:07 
# @Author : for 
# @File : 17_sheet-test.py 
# @Software: PyCharm
import xlsxwriter

workbook = xlsxwriter.Workbook('./static/demo1.xlsx')

worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('foglio2')
worksheet3 = workbook.add_worksheet('data')
worksheet4 = workbook.add_worksheet()

workbook.close()