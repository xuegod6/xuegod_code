# -*- coding: utf-8 -*-
# @Time : 2019/1/22 20:36 
# @Author : for 
# @File : 01_del_test.py 
# @Software: PyCharm
# class Hero:
#     def __del__(self):
#         print('英雄已经阵亡')
# man1 = Hero()
# print('程序结束')

# print('^^^^^^^^^^^^^^^^^^^^^^')

class Hero:
    def __del__(self):
        print('英雄已经阵亡')
man1 = Hero()
man2 = man1
del man1
del man2
print('程序结束')