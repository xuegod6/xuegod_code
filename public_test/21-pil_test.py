# -*- coding: utf-8 -*-
# @Time : 2018/12/15 10:08 
# @Author : for 
# @File : 21-pil_test.py 
# @Software: PyCharm
from PIL import Image

im = Image.open('./static/2.png')

box =(0,0,100,100)

im_corp = im.crop(box)

im.paste(im_corp,(100,100))
im.paste(im_corp,(400,400,500,500))

im.show()

# n_im = Image.new(im.mode,(400,300),'yellow')
#
# n_im.show()