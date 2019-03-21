import requests

response = requests.get('http://httpbin.org/get')
print(response.text)
print(response.json())  #response.json()方法同json.loads(response.text)
print(type(response.json()))