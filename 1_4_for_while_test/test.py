# -*- coding: utf-8 -*-
# @Time : 2019/1/4 20:11 
# @Author : for 
# @File : test.py 
# @Software: PyCharm
#coding = utf-8
import wx
import random
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"My Frame",size = (766, 485),
                          style = wx.DEFAULT_FRAME_STYLE)
		#创建画布
        self.panel = wx.Panel(self)
	#事件绑定
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        self.SetMaxSize((766, 485))
        self.SetMinSize((766, 485))
        #设置文本 并设置颜色
        self.StaticText = wx.StaticText(self.panel,pos = (320,70),size = (144,27))
        self.StaticText.SetBackgroundColour("white")
		#设置是否透明
        self.StaticText.SetTransparent(0)
		#设置字体
        self.staticFont = wx.Font(22,wx.DECORATIVE,wx.NORMAL,wx.BOLD)
        self.StaticText.SetFont(self.staticFont)
        #创建一个绘图对象
        buttonBmp = wx.Image("buttonBack.jpg", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        #设置按钮，按钮为一个图片，绑定一个事件
        self.button = wx.BitmapButton(self.panel,bitmap = buttonBmp,pos = (265,315))
        self.button.Bind(wx.EVT_BUTTON,self.GetName)
       #c lientDc（）该函数检索指定窗口的客户区域或整个屏幕的显示设备上下文环境的句柄，以后可以使用该句柄来在设备上下文环境中绘图。
    def OnEraseBack(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
#返回指定窗口的部分的损坏区域。GetBox返回区域的外部边界
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("loveBack.jpg")
       #在指定的点上以及上下文中绘制图
        dc.DrawBitmap(bmp, 0, 0)
    def GetName(self,event):
        with open("name.txt","rb") as f:
             lines = f.readlines()
             names = random.choice(lines)
