# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 14:38
# @Author  : for 
# @File    : 01_pip_test0.py
# @Software: PyCharm
# from PIL import Image
# #打开文件
# im = Image.open('1.jpg')
# #展示图片
# im.show()


# from PIL import Image
#
# im = Image.open('1.jpg')
# #获原图的size
# width,height = im.size
# #利用方法，缩小50%
# im.thumbnail((width//2,height//2))
# #保存到本地
# im.save('aaa.png')

# from PIL import Image
#
# im = Image.open('1.jpg')
#
# box = (0,0,100,100)
#
# im_crop = im.crop(box)
# print(im_crop.size,im_crop.mode)
# im.paste(im_crop,(100,100))
# im.paste(im_crop,(400,400,500,500))
#
# im.show()


from PIL import Image
import pytesseract
img = Image.open('2.png')
img = img.convert('L')
result = pytesseract.image_to_string(img)
print(result)
#汉语






