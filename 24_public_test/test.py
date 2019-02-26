# -*- coding: utf-8 -*-
# @Time : 2018/12/24 14:05 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
import requests,json
# url = 'https://www.instagram.com/'
urls = []
headers = {
'referer': 'https://www.instagram.com/',
'cookie': 'mid=XCCjfgALAAHUnsWCm4X-HC6maX8d; mcd=3; csrftoken=lY5HlF4pQSZZ1Lv0KPeCnXnQJdfrGh9k; ds_user_id=9858126089; sessionid=9858126089%3AuXolNIvhGsSFIF%3A18; rur=ATN; urlgen="{\"47.74.224.3\": 45102}:1gbMVE:xQYFg-xey4_L7kWwbLdq4aBBT-Y"',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}
url = 'https://www.instagram.com/graphql/query/?query_hash=01b3ccff4136c4adf5e67e1dd7eab68d&variables=%7B%22fetch_media_item_count%22%3A12%2C%22fetch_media_item_cursor%22%3A%22KA0BBAAQAAgA5___AIEEFpDn8vj7WSoUBAA%3D%22%2C%22fetch_comment_count%22%3A4%2C%22fetch_like%22%3A3%2C%22has_stories%22%3Afalse%7D'
def get_urls(url):
    try:
        response = requests.get(url=url,headers=headers)
        if response.status_code == 200:
            return  response.text
        else:
            print('请求装填',response.status_code)
    except Exception as e:
        print(e)
        return  None
json_data = json.loads(get_urls(url))
infos = json_data['data']['user']['edge_web_feed_timeline']['edges']
for i,j in enumerate(infos):
    print()
    name = str(i)+'.png'
    data = requests.get(j['node']['display_url']).content
    with open(name,'wb') as f:
        f.write(data)

    # print(display_url)