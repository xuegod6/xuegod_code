# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 21:46
# @Author  : for 
# @File    : 06_queue_test.py
# @Software: PyCharm
import multiprocessing,time
if __name__ == '__main__':
    queue = multiprocessing.Queue(3)
    #放入数据
    queue.put(1)
    queue.put('hello')
    queue.put([3,5])
    # 总结: 队列可以放入任意数据类型
    # 提示： 如果队列满了，需要等待队列有空闲位置才能放入数据，否则一直等待
    # queue.put((5,6))
    # 提示： 如果队列满了，不等待队列有空闲位置，如果放入不成功直接崩溃
    # queue.put_nowait((5,6))

    print(queue.full())
    #查看队列是否空了 这个非常不可靠
    print(queue.empty())
    #解决方法，1.加延迟 @ 使用队列的个数不适用empty
    #time.sleep(0.01)
    if queue.qsize() == 0:
        print('队列为空')
    else:
        print('队列不为空')

    size = queue.qsize()
    print('这个队列的大小：',size)


    value = queue.get()
    print('得到数据:',value)

    value = queue.get()
    print('得到数据:',value)

    value = queue.get()
    print('得到数据:',value)

    size = queue.qsize()
    print('这个队列的大小：',size)

    value = queue.get_nowait()
    print(value)