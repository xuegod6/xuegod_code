# -*- coding: utf-8 -*-
# @Time : 2019/1/10 16:58 
# @Author : for 
# @File : 03_bilibili_test.py 
# @Software: PyCharm
import requests
import random
import time

def get_json(url):
    #模拟请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    #发送的参数
    params = {
        'page_size':10,
        'next_offset':str(num),
        'tag':'今日热门',
        'platform':'pc'
    }
    try:
        #的钓json文本
        html = requests.get(url, params=params, headers=headers)
        # 返回得到json数据
        return html.json()

    except :
        print('很遗憾没有得到json数据')

def download(url, path):
    size = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    #进行访问
    response = requests.get(url, headers=headers, stream=True)  # stream属性必须带上
    chunk_size = 1024   # 规定每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 总大小
    if response.status_code == 200:
        print('视频文件大小:%0.2f MB' % (content_size/chunk_size/1024))  # 换算单位
        #这个是我们打开视频并保存
        with open(path, 'wb') as file:
            #迭代读取规定打下小的数据
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                size += len(data)  # 已下载的文件大小
                # print('已下载文件的大小:',size)

if __name__ == '__main__':
    for i in range(10):
        #起始的url地址
        url = 'http://api.vc.bilibili.com/board/v1/ranking/top?'
        #这个为了更改get_json中的数据不同组的数据
        num = i * 10 + 1
        #调用方法返回json文本！
        html = get_json(url)
        #获取返回json格式重点 data 下的items，infos是一个列表
        infos = html['data']['items']
        #对列表进行遍历
        for info in infos:
            # 小视频的标题
            title = info['item']['description']
            # 小视频的下载链接
            video_url = info['item']['video_playurl']
            print('本次下载视频标题:',title)
            # 接下来我们上面拿到地址之后就可以视频下载
            try:
                #调用下载download方法！里面分别对应的是视频的链接地址，还有本地存储地址
                download(video_url, path='./video/'+'%s.mp4' % title)
                print('视频下载状态:','success!')
            except BaseException:
                print('视频下载状态:','bad!')
                pass
            time.sleep(2)
        time.sleep(int(format(random.randint(2, 8))))  # 设置随机等待时间
# class Spider()