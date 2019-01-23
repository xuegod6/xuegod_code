# -*- coding: utf-8 -*-
# @Time : 2019/1/22 21:40 
# @Author : for 
# @File : 05_open_test.py 
# @Software: PyCharm

# f = open('1.txt','r',encoding='utf-8')
# #判断是否关闭
# print(f.closed)
# #打印权限
# print(f.mode)
# #打印文件的name
# print(f.name)
# #文件关闭
# f.close()
# f = open('1.py','r',encoding='utf-8')
# #读取所有内容
# # print(f.read(10))
# #读取一行
# # print(f.readline())
# #读取所有 并且按照list承载
# print(f.readlines())
#
# f.close()

#
# f = open('2.txt','wb')
# f.write('你好呀，hello,world')
# # f.writelines(str(i)+'\n' for i in range(10))
# # f.writelines(['a','b','c'])
# f.close()



try:
    f = open('2.txt', 'r',encoding='utf-8')
    print(f.read())
except Exception as e:
    print(e)
finally:
    # f.close()
    pass
print(f.closed)






