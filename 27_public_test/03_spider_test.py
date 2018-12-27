# -*- coding: utf-8 -*-
# @Time : 2018/12/27 14:49 
# @Author : for 
# @File : 03_spider_test.py 
# @Software: PyCharm
# from urllib import request
#
# import requests,time
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1545892906631='
#
# headers = {
# 'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1545892872367_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
# }
# data_str='''
# tn: resultjson_com
# ipn: rj
# ct: 201326592
# is:
# fp: result
# queryWord: 大美女
# cl: 2
# lm: -1
# ie: utf-8
# oe: utf-8
# adpicid:
# st: -1
# z:
# ic: 0
# hd:
# latest:
# copyright:
# word: 大美女
# s:
# se:
# tab:
# width:
# height:
# face: 0
# istype: 2
# qc:
# nc: 1
# fr:
# expermode:
# force:
# pn: 30
# rn: 60
# gsm: 1e
# 1545892906631:
# '''
# send_data = {}
#
# for line in data_str.splitlines():
#     # print(line)
#     line_data = line.split(': ')
#     # print(line_data)
#     if len(line_data) == 2:
#         key,value = line_data
#         if key and value:
#             send_data[key] = value
#         # print(key)
# # print(send_data)
#
# response = requests.get(url=url,headers=headers,params=send_data)
# # print(response)
# # print(response.text)
# content = response.json()['data']
# for index,src in enumerate(content):
#     # pass
#     img_url = src.get('middleURL')
#     # print(img_url)
#     if img_url:
#         name = './image/image_%s_%s.png'%('唯美',index)
#         try:
#             request.urlretrieve(url=img_url,filename=name)
#         except Exception as e:
#             print(e)
#         else:
#             print('%s is download'%name)
#         time.sleep(1)

# print(content)
def get_image(keywords):
    from urllib import request

    import requests, time
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%94%AF%E7%BE%8E&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=%E5%94%AF%E7%BE%8E&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=1e&1545892906631='

    headers = {
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1545892872367_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%94%AF%E7%BE%8E',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    data_str = '''
    tn: resultjson_com
    ipn: rj
    ct: 201326592
    is: 
    fp: result
    queryWord: 大美女
    cl: 2
    lm: -1
    ie: utf-8
    oe: utf-8
    adpicid: 
    st: -1
    z: 
    ic: 0
    hd: 
    latest: 
    copyright: 
    word: 大美女
    s: 
    se: 
    tab: 
    width: 
    height: 
    face: 0
    istype: 2
    qc: 
    nc: 1
    fr: 
    expermode: 
    force: 
    pn: 30
    rn: 60
    gsm: 1e
    1545892906631: 
    '''
    send_data = {}

    for line in data_str.splitlines():
        # print(line)
        line_data = line.split(': ')
        # print(line_data)
        if len(line_data) == 2:
            key, value = line_data
            if key and value:
                send_data[key] = value
            # print(key)
    # print(send_data)
    send_data['word'] = send_data['queryword'] = keywords
    response = requests.get(url=url, headers=headers, params=send_data)
    # print(response)
    # print(response.text)
    content = response.json()['data']
    for index, src in enumerate(content):
        # pass
        img_url = src.get('middleURL')
        # print(img_url)
        if img_url:
            name = './image/image_%s_%s.png' % ('唯美', index)
            try:
                request.urlretrieve(url=img_url, filename=name)
            except Exception as e:
                print(e)
            else:
                print('%s is download' % name)
            time.sleep(1)
if __name__ == '__main__':
    key = input('请输入你想爬取的内容')
    get_image(key)