import requests

response =requests.get('http://imgs.julive.com/l?p=eyJpbWdfcGF0aCI6IlwvVXBsb2FkXC8wMjAxNS01LTAxOC0wMTYtMDU1LTAzOS0wMTYtNDQ5LmpwZyIsImltZ19wYXJhbV9hcnIiOltdLCJ4LW9zcy1wcm9jZXNzIjoiXC9yZXNpemUsd181MjAsaF8zNTAsbV9maWxsIn0%3D')
b= response.content
with open("fengjing.jpg","wb") as f:
    f.write(b)