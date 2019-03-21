import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)
print(type(response.cookies))
for k,v in response.cookies.items():
    print(k+":"+v)