import _thread
import time
# 为线程定义一个函数
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
# 创建两个线程
#但是这个模块我们不推荐，因为底层封装的时候它的主线程不会等待子线程的结束！
#官方以及我们推荐再封装Threading，所以在这里大家了解下
try:
    _thread.start_new_thread( print_time,("Thread-1", 2, ) )
    _thread.start_new_thread( print_time,("Thread-2", 4, ) )
except:
    print ("Error: 无法启动线程")
while True:
    pass
