# -*- coding: utf-8 -*-
# @Time : 2018/12/5 14:17 
# @Author : for 
# @File : 01_read_test.py 
# @Software: PyCharm
# with open('2.py')as f:
#
#     print(f.read())
# class A:
#
#     def __enter__(self):
#         print('__enter__() is called')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#
#         print('__exit__() is called')
#
# with A() as a:
#
#     print('gpt instance')
#
# with open('1.png','rb') as png1:
#
#     with open('2.png','wb') as png2:
#
#         png2.write(png1.read())
#
# f = open('cnword.txt',encoding='utf-8')
# print(f.readline())
# pos = f.tell()
# print('当前的指针位置%s'%pos)
# f.seek(0,0)
# print(f.readline())
# f.seek(0,1)
# pos = f.tell()
# print('当前的指针位置%s'%pos)
#
# f.close()



# 读取文章
import time
def reader(path,line = 3):
    #打开文件
    with open(path,'r',encoding='utf-8') as f:
        #指针指向文件的末尾
        f.seek(0,2)
        #指纹末尾的位置
        end = f.tell()
        #指针又指向的文件开头
        f.seek(0.0)
        #处理开启自动
        auto = str(input('是否开启自动：(y/n)?'))
        #判断 自动
        if auto == 'y':
            #死循环，不断打印
            while True:
                #line= 3 循环三次
                for i in range(line):
                    #每次打印一行
                    print(f.readline())
                #为了视觉上的享受，我们停顿2秒
                time.sleep(2)
                #如果此时的指针指向最后一个字节
                if f.tell() == end:
                    break
        else:
            #定义个变量N
            con = 'N'
            #指针指向末尾
            f.seek(0,2)
            #获取指针的位置（执行那个末尾的位置）
            end  = f.tell()
            #指针指向开头
            f.seek(0,0)
            #开始循环
            while True:
                #如果判断可以
                if con == 'N':
                    #循环三次 打印三行
                    for i in range(line):
                        print(f.readline())
                else:
                    print('头铁是不？')
                #判断 指针指向最后的位置
                if f.tell() == end:
                    break
                con = input('>>>')
reader('cnword.txt')










