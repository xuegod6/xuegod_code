import time
try:
    f = open('123.txt',encoding='utf-8')
    try:
        while True:
            #自动打印三行
            for i in range(3):
                print(f.readline())
                #睡两秒
            time.sleep(2)
            #再读一行
            content = f.readline()
            #打印
            print(content)
            #如果我们读取的内容0 则break
            if len(content) == 0:
                break
    #无论如何都要关闭文件
    finally:
        f.close()
except:
    print('没有这个文件')
