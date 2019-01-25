
# print('----test01----')
# open('123.txt','r')
# print('----test02----')
# print('----test01-----')
# try:
#     print(name) #没有变量
#     open('123.txt','r')#没有文件
#     print('---try---')
# except FileNotFoundError:
#     print('这是一个FileNotFoundError的错误:%s'%FileNotFoundError)
# except NameError:
#     print('这是一个Nameerror的错误:%s'%NameError)
#
# print('-----test02----')

# 方法一：指定一个通用异常，在这里我们使用所有的异常的父类Exception达到我们想要的结果

# 语法：
# try:
#     语句块
# except Exception:
#     语句块
# print('----start-----')
# try:
#     print(name) #没有变量
#     open('123.txt','r')#没有文件
#     print('---try---')
# except (NameError,FileNotFoundError,TypeError,IOError):
#     print('这是一个FileNotFoundError的错误:%s'%Exception)
#     print('这是一个Nameerror的错误:%s'%NameError)
#     print('这是一个TypeError的错误:%s'%TypeError)
#     print('这是一个IOError的错误:%s'%IOError)
# # except NameError:
# #     print('这是一个Nameerror的错误:%s'%NameError)
# print('-----end----')

# 方法三：except子句后不带任何异常名称，捕获所有异常
try:
    print(a)
    open('123.txt','r')
except:
    print('有异常，但是哥哥就不想打印……')










