# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:43
# @Author  : for 
# @File    : 04_filr_read_test.py
# @Software: PyCharm
import pyttsx3
with open('2.txt','r',encoding='utf-8') as f:
    line = f.read()
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume',volume-0.25)
    engine.say(line)
    engine.runAndWait()