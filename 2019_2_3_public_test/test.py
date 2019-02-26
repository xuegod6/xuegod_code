# L = []
# while True:
#     text = input('请输入想要输入的内容:')
#     if text:
#         L.append(text)
#         print(L)
#     print('计算输入的几行内容')
#     len_text = len(L)
#     print(len_text)
#     print('开始计算总共字符')
#     num_str = 0
#     for data in L:
#         num_str += len(data)
#     print(num_str)
#     if text=='':
#         break

num = int(input('请输入一个整数：'))
for i in range(1,num+1):
    print(' '* (num - i )+(2*i-1)*'*')
a = num
while a > 0:
    print((num-1)*' '+'*')
    a -= 1