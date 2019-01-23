# -*- coding: utf-8 -*-
# @Time : 2019/1/22 22:30 
# @Author : for 
# @File : 08_电子书_test.py 
# @Software: PyCharm
import time
def reader(path,line = 3):
    #打开文件读取
    with open(path,'r',encoding='gbk') as f:
        #我们把指针指向文件的末尾
        f.seek(0,2)
        #告诉我文件末尾的指针的位置总字节量
        end = f.tell()
        #指针指向开头
        f.seek(0,0)
        #你是否要开启自动？
        auto = input('是否开启自动:(y/n)?')
        if auto == 'y':#是
            while True:#深度循环
                #循环三次 读取三行
                for i in range(line):
                    print(f.readline())
                time.sleep(2)#美都区三行会sleep2两秒
                # 判断如果你的文件指针指向文件末尾 我就强制break
                if f.tell() == end:
                    break
        else:
            con = 'N'
            f.seek(0,2)
            end = f.tell()
            f.seek(0,0)
            while True:
                if con == 'N':
                    for i in range(line):
                        print(f.readline())
                else:
                    print('请输入N')
                if f.tell() == end:
                    break
                con = input('>>>')
reader('1.txt')
