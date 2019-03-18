import requests
from fake_useragent import UserAgent
url = 'https://www.zhihu.com/question/29024583'
ua = UserAgent()
headers = {
    'User-Agent':ua.random,
}
res = requests.get(url= url,headers=headers)
html = res.text
