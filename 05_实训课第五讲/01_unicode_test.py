u  = '学神'
#python 编码是‘gbk
str1 = u.encode('gbk')
print(str1)
#python3 编码 ‘utf-8’
str2 = u.encode('utf-8')
print(str2)
#解码
u1 = str1.decode('gbk')
print(u1)
#解码
u2 = str2.decode('utf-8')
print(u2)