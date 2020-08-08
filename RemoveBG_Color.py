# coding:utf-8
from cutbg.API_removebg import API_removebg
from PIL import Image

import traceback
import os

#                                                   #
#   本项目用于使用RemoveBG的API进行证件照背景色替换    #
#                                                   #

# API KEY
APIkey = "swgmh9EQKCxBbEv52CJMqNpE"

# 输入 -- 需要修改的图片，请放在img文件夹下
Imgname = "sunxiaochuan.jpeg"
# 输出 -- 填空则为默认地址out/ans.png
outImagePath = ""

# 需要替换的颜色 RGB 值
changeColor = (255, 255, 255)  # 白色


folder = os.getcwd() + '\\img\\'
Imgpath = folder+Imgname

if(not os.path.exists(folder)):
    os.makedirs(folder)
    print("Create successful folder")

try:
    print(Imgpath)
    API_removebg(APIkey, Imgpath).API_RMBG_use()
except Exception:
    with open('./error.log', 'a') as f:
        f.write('background remove fail :'+traceback.format_exc())
        print("Error: See error.log and you will know what happen")
        exit(0)

# 输入已经去除背景的图像
new_Imgpath = Imgpath+"_no_bg.png"
im = Image.open(new_Imgpath)
x, y = im.size

try:
    # 填充红色背景
    p = Image.new('RGBA', im.size, changeColor)
    p.paste(im, (0, 0, x, y), im)
    # 保存填充后的图片
    if outImagePath == "":
        p.save('./out/ans.png')
    else:
        p.save(outImagePath)
except Exception:
    with open('./error.log', 'a') as f:
        f.write('background change fail :'+traceback.format_exc())
        print("Error: See error.log and you will know what happen")

print("fill color Done")
