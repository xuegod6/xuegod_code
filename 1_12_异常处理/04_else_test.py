


try:
    num= 10
    print(num)
except Exception as e:
    print('有异常，……%s'%e)
else:
    print('没有发生异常')
finally:
    print('__finally__')