# -*- coding: utf-8 -*-
# @Time : 2018/12/15 10:29 
# @Author : for 
# @File : 22-yanzhengma _test.py 
# @Software: PyCharm

from PIL import Image
import pytesseract

img = Image.open('./static/1.png')

img = img.convert('L')

result = pytesseract.image_to_string(img)

print(result)
