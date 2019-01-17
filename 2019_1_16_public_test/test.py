# import time
# import greenlet
# def work1():
#     for i in range(5):
#         print('work1...')
#         time.sleep(0.2)
#         #切换到协程2里面执行对应的任务
#         g2.switch()
# #任务2
# def work2():
#     for i in range(5):
#         print('work2...')
#         time.sleep(0.2)
#         #切换到第一个协程执行对应的任务
#         g1.switch()
# if __name__ == '__main__':
#     #创建协程指定的对应任务
#     g1 = greenlet.greenlet(work1)
#     g2 = greenlet.greenlet(work2)
#     #切换到第一个协程执行对应的任务
#     g1.switch()

# import gevent
# def work(n):
#     for i in range(n):
#         # 获取当前协程
#         print(gevent.getcurrent(), i)
#         gevent.sleep(1)
# g1 = gevent.spawn(work, 5)
# g2 = gevent.spawn(work, 5)
# g3 = gevent.spawn(work, 5)
# g1.join()
# g2.join()
# g3.join()






# import gevent
# import time
# from gevent import monkey
#
# # 打补丁，让gevent框架识别耗时操作，比如：time.sleep，网络请求延时
# monkey.patch_all()
# # 任务1
# def work1(num):
#     for i in range(num):
#         print("work1....")
#         time.sleep(0.2)
#         # gevent.sleep(0.2)
#
# # 任务1
# def work2(num):
#     for i in range(num):
#         print("work2....")
#         time.sleep(0.2)
#         # gevent.sleep(0.2)
#
# if __name__ == '__main__':
#     # 创建协程指定对应的任务
#     g1 = gevent.spawn(work1, 3)
#     g2 = gevent.spawn(work2, 3)
#
#     # 主线程等待协程执行完成以后程序再退出
#     g1.join()
#     g2.join()
#




# import gevent
# import time
# from gevent import monkey
#
# # 打补丁，让gevent框架识别耗时操作，比如：time.sleep，网络请求延时
# monkey.patch_all()
#
#
# # 任务1
# def work1(num):
#     for i in range(num):
#         print("work1....")
#         time.sleep(0.2)
#         # gevent.sleep(0.2)
#
# # 任务1
# def work2(num):
#     for i in range(num):
#         print("work2....")
#         time.sleep(0.2)
#         # gevent.sleep(0.2)
#
#
#
# if __name__ == '__main__':
#     # 创建协程指定对应的任务
#     g1 = gevent.spawn(work1, 3)
#     g2 = gevent.spawn(work2, 3)
#
#     while True:
#         print("主线程中执行")
#         time.sleep(0.5)

import gevent
import urllib.request # 网络请求模块
from gevent import monkey

# 打补丁： 让gevent使用网络请求的耗时操作，让协程自动切换执行对应的下载任务
monkey.patch_all()

# 根据图片地址下载对应的图片
def download_img(img_url, img_name):
    try:
        print(img_url)
        # 根据图片地址打开网络资源数据
        response = urllib.request.urlopen(img_url)
        # 创建文件把数据写入到指定文件里面
        with open(img_name, "wb") as img_file:
            while True:
                # 读取网络图片数据
                img_data = response.read(1024)
                if img_data:
                    # 把数据写入到指定文件里面
                    img_file.write(img_data)
                else:
                    break
    except Exception as e:
        print("图片下载异常:", e)
    else:
        print("图片下载成功: %s" % img_name)


if __name__ == '__main__':
    # 准备图片地址
    img_url1 = "https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=551346117,2593226454&fm=27&gp=0.jpg"
    img_url2 = "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=829730016,3409799239&fm=27&gp=0.jpg"
    img_url3 = "https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1815077192,817368579&fm=27&gp=0.jpg"
    # 创建协程指派对应的任务
    g1 = gevent.spawn(download_img, img_url1, "1.jpg")
    g2 = gevent.spawn(download_img, img_url2, "2.jpg")
    g3 = gevent.spawn(download_img, img_url3, "3.jpg")
    # 主线程等待所有的协程执行完成以后程序再退出
    gevent.joinall([g1, g2, g3])



