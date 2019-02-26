# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 14:25
# @Author  : for 
# @File    : 04_weixin_test.py
# @Software: PyCharm
from wxpy import * # 导入模块
bot = Bot(cache_path=True) # 初始化机器人，扫码登陆，但每次登陆都得重新扫码
#bot = Bot(cache_path=True)
#把登录信息保存下来，不想每次都扫码的可以用这一条
# friend = bot.friends().search(u'陈玉文')[0]
# friend.send(u'这是一个微信接口测试')
# tuling = Tuling(api_key='958ea815206946f18bc360564e47a4d8')
# @bot.register(msg_types=TEXT)
# def reply_msg(msg):
#     msg.reply(msg)
# # embed()
# bot.join()