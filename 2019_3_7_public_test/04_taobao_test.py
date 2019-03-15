import requests


host = 'http://ali-voice.showapi.com'
path = '/createTemplate'
method = 'GET'
appcode = '94d78954209549eaa1ede3a625ad41d1'
querys = 'content=%7B%22userName%22%3A%22%E5%BC%A0%E4%B8%89%22%2C%22mailNo%22%3A%22610349360550%22%7D&notiPhone=17611100746'
bodys = {}
url = host + path + '?' + querys
headers = {
    'Authorization':'APPCODE ' + appcode
}
response = requests.get(url,headers=headers)
content = response.content
if (content):
    print(content)