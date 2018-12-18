# with open('test.py','w+') as f:
#     f.write('abc\n')

with open('test.py','w+') as f:
    f.write('123')
    f.seek(0,0)
    print(f.read())