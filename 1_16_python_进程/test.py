import multiprocessing
import time

# 测试子进程是否执行完成以后主进程才能退出
def work():
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)

if __name__ == '__main__':
    # 创建子进程
    work_process = multiprocessing.Process(target=work)
    work_process.start()
    #如果不加 work_process.join()
    work_process.join()
    # 让主进程等待1秒钟
    print('开始等待')
    time.sleep(1)
    print("主进程执行完成了啦")
