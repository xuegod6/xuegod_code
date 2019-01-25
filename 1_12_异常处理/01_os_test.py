# import os
# print(os.path.isfile('test.py'))
# print(os.path.isdir('test.py'))
# print(os.path.isdir('xuegod'))
# print(os.path.exists('1.txt'))
# print(os.path.split('E:/xuegod/python3'))
#更改文件目录
# print('返回本地路径:',os.getcwd())
# path = './xuegod/'
# os.chdir(path)
# print('新的本地路径:',os.getcwd())
# os.chdir(r'E:\xuegod_code\1_12_异常处理')
# print(os.getcwd())
#获得自文件大小
# print(os.path.getsize('test.py'))
# print(os.path.abspath('test
# .py'))

# import os
# file_path = os.getcwd()
# print(file_path)
# new_path = os.path.join(file_path,'1.txt')
# print(new_path)

#os.walk
# import os
# #获取当前路径
# path = os.getcwd()
# #返回的是文件夹本身的地址 目录文件
# for root,dirs,files in os.walk(path):
#     print(dirs)
#     for filename in files:
#         print(os.path.join(root,filename))

# 如何批量修改文件夹下的文件名？（面试题）

# import os
# m_name = os.listdir('./xuegod/')
# for temp in m_name:
#     new_name = 'xuegod_'+ temp
#     os.rename('./xuegod/'+temp,'./xuegod/'+new_name)


# 4.3  实战
# 传入一个文件路径，得到该路径下所有的文件目录?（面试题）
import os
def iterbrowse(path):
    #返回文路径 目录 文件
    for home,dirs,files in os.walk(path):
        #对文件进行遍历
        for file in files:
            #路径拼接
            print(os.path.join(home,file))
#处理文件路径
new_path = os.getcwd()
#调用
iterbrowse(new_path)


















