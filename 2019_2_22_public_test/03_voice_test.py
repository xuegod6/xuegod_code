# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:28
# @Author  : for 
# @File    : 03_voice_test.py
# @Software: PyCharm
import pyttsx3
engine = pyttsx3.init()
#主要获取咱们微软的声音
volume = engine.getProperty('volume')
engine.setProperty('volume',volume-0.7)
#对声音进行遍历
engine.say('这是一条神奇的前途哎呦，哎呦不错呦')

engine.runAndWait()
