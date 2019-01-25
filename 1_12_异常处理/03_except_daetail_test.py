

# 1. as 打印详细信息
# try:
#     print(a)
# except NameError as e:
#     print('NameError 的详细信息为%s'%e)


print('----start-----')
try:
    print(name) #没有变量
    open('123.txt','r')#没有文件
    print('---try---')
except (NameError,FileNotFoundError) as e:
    # print('这是一个FileNotFoundError的错误:%s'%Exception)
    # print('这是一个Nameerror的错误:%s'%NameError)
    print('详细信息为%s'%e)
# except NameError:
#     print('这是一个Nameerror的错误:%s'%NameError)
print('-----end----')