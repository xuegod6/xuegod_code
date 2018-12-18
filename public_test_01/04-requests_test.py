# -*- coding: utf-8 -*-
# @Time : 2018/12/18 14:28 
# @Author : for 
# @File : 04-requests_test.py 
# @Software: PyCharm
import time
from urllib import request
import requests

def get_image(keywords,num):
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&selected_tags=&cg=girl&pn=510&rn=30&gsm=1fe&1545114043518='

    headers = {
    'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }

    data_str = '''
    tn: resultjson_com
    ipn: rj
    ct: 201326592
    is: 
    fp: result
    queryWord: 唯美
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
    word: 美女
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
    selected_tags: 
    pn: 60
    rn: 60
    gsm: 3c
    1545114685662: 
    '''
    send_data = {}

    for line in data_str.splitlines():
        line_data = line.split(': ')
        if len(line_data) == 2:
            key,value = line_data
            if key and value:
                send_data[key] = value
    send_data['queryWord'] = send_data['word'] = keywords
    send_data['rn'] = str(30*num)
    response = requests.get(url=url,headers=headers,params=send_data)

    content = response.json()['data']
    # for i in content:
    #     print(i['middleURL'])
    # # print(content)

    for index,src in enumerate(content):
        img_url = src.get('middleURL')
        if img_url:
            name = './image/image_%s_%s.png'%('唯美',index)
            try:
                request.urlretrieve(url=img_url,filename=name)
            except Exception as e:
                print(e)
            else:
                print('%s is down'%name)
            time.sleep(1)

if __name__ == '__main__':
    keywords = input('请输入你想输入的内容：')
    num = int(input('请输入你要的数字'))
    get_image(keywords,num)
    # print(line_data)
    # print(line)







