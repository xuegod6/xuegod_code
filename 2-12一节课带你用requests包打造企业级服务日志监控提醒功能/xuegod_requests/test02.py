import requests
data = {
    'name':'if',
    'age':'18'
}
response = requests.get("http://httpbin.org/get",params=data)
print(response.text)