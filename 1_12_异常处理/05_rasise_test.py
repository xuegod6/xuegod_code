# class Test(object):
#     def start(self):
#         try:
#             content = int(input('请输入一个数字:'))
#             if content < 5:
#                 #raise 抛出异常后，后面的代码不在执行
#                 raise Exception('输入的数字小于3')
#                 # print('异常已经抛出')
#         #except后面的异常和raise抛出的一样
#         except Exception as info:
#             print(info)
#         else:
#             print('恭喜你没有异常')
# t = Test()
# t.start()

from imp_except import MyException
# s = MyException(2,3)
# print(s.num)
class Test(object):
    def start(self):
        try:
            content = int(input('请输入一个数字:'))
            if content < 5:
                #raise 抛出异常后，后面的代码不在执行
                raise MyException(content,3)
                # print('异常已经抛出')
        #except后面的异常和raise抛出的一样
        except MyException as s:
            print('当前大小:%s，最小的数字:%s'%(s.num,s.atleast))
        else:
            print('恭喜你没有异常')
t = Test()
t.start()















