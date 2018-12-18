# -*- coding: utf-8 -*-
# @Time : 2018/12/5 13:44 
# @Author : for
# @File : 01_zipfile_test.py 
# @Software: PyCharm
import zipfile

azip = zipfile.ZipFile('1.zip','w')

azip.write('1/2.txt',  compress_type=zipfile.ZIP_LZMA)

azip.close()
#
# # print(azip.namelist())
# #
# # print(azip.filename)
#
# azip_info = azip.getinfo('1/cnword.txt')
#
# # print(azip_info.file_size)
# #
# # print(azip_info.compress_size)
# #
# # print('压缩率{:.2f}'.format(azip_info.file_size/azip_info.compress_size))
#
# a = azip.read('1/cnword.txt')
# print(a.decode())
#
#
# azip.extractall('./static/')
#
# azip.close()