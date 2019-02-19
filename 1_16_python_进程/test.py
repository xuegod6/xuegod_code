with open('./copy/1.py','rb') as f:
    with open('./copy_in/1.py','wb') as e:
        e.write(f.read())