#By WhitemuTeam(Github)
#安装库：pip install opencv-python/pip install PySimpleGUI

import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import PySimpleGUI as sg

#GUI
layout = [[sg.Text('请输入新人的用户名:')],
          [sg.Input()],
          [sg.Button('提交')]]

window = sg.Window('欢迎新人表情包生成', layout, icon=r'LOGO.ico') #设置窗口
event, value = window.Read() #读取输入值
name = value[0]
word = '欢迎'+name+'进群' #生成第一行句子
namehigh = len(name) #判断用户名长度

# 编辑图片路径
bk_img= cv2.imread("first.jpg")
#设置需要显示的字体
fontpath= "HarmonyOS_Sans_SC_Black.ttf"
if namehigh < 8:
	font= ImageFont.truetype(fontpath,32) # 32为字体大小
else:
	font= ImageFont.truetype(fontpath,25)
img_pil= Image.fromarray(bk_img)
draw= ImageDraw.Draw(img_pil)
#绘制文字信息# (100,300)为字体的位置，(255,255,255)为颜色RGB码
draw.text((70,230), word, font= font, fill= (0,0,0))
bk_img= np.array(img_pil)
 
cv2.imshow("finally",bk_img) #展示图片
cv2.waitKey()# 保存图片路径
cv2.imwrite("finally.jpg",bk_img)#输出图片



