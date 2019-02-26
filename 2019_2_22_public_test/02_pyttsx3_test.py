# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:12
# @Author  : for 
# @File    : 02_pyttsx3_test.py
# @Software: PyCharm
import pyttsx3
#生成一个语音驱动，
engine = pyttsx3.init()
#利用语音驱动，说话
engine.say('大家好，我是for老师，我在学神IT')
engine.say('啊，啊啊啊啊，哎呦，啊呀')
#语音驱动运行并等待
engine.runAndWait()