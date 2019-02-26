# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 10:09
# @Author  : for 
# @File    : 01_api_test.py
# @Software: PyCharm
import win32com.client

speaker = win32com.client.Dispatch('SAPI.SpVoice')

speaker.Speak('Hello ,I am the king of the world')
