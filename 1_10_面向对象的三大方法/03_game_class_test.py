# -*- coding: utf-8 -*-
# @Time : 2019/1/19 21:06 
# @Author : for 
# @File : 03_game_class_test.py 
# @Software: PyCharm
# 简单的游戏，利用一个类创建Game，
# 要求：
# 1、	玩家可以自己输入自己的名字和姓名。
# 2、	登录后开始游戏就会打印“帮助信息”
# 3、	帮助信息的下方会出现最高分
# 4、	启动游戏会打印欢迎字句
# 5、	利用类方法，静态方法完成
class Game(object):
    def __init__(self,player_name):
        self.player_name = player_name
        Game.show_help()
        Game.show_top_score()
    @staticmethod
    def show_help():
        print('--------------')
        print('|查看帮助信息|')
        print('--------------')
    @classmethod
    def show_top_score(cls):
        print('-------------')
        print('|最高分：1111|')
        print('--------------')
    def start_game(self):
        print('%s 开始游戏'%(self.player_name))
if __name__ == '__main__':
    tom = Game('for')
    tom.start_game()






