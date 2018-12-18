# -*- coding: utf-8 -*-
# @Time : 2018/12/5 15:33 
# @Author : for 
# @File : 01_zip_test.py 
# @Software: PyCharm
import zipfile

azip = zipfile.ZipFile('1.zip')

# print(azip.namelist())
#
# print(azip.filename)
# azip_info = azip.getinfo('1/cnword.txt')
azip.extractall('./static/')


# a = azip.read('1/cnword.txt')
#
# print(a.decode())

# print(azip_info.file_size)
# print(azip_info.compress_size)
#
# print('压缩率%.2f'%(azip_info.file_size/azip_info.compress_size))
azip.close()