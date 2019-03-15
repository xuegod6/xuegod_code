import hashlib

md5 = hashlib.md5()
md5.update('123456salt'.encode())
print(md5.hexdigest())