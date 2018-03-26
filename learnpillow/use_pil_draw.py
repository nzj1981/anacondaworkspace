# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_pil_draw.py 
@time: 2018/3/26 15:17
"""

'''
利用PIL的ImageDraw绘图方法,要求生成字母验证码图片
'''

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

# 创建Font对象, 注意arial.ttf根据系统环境不一样,需要全路径
font = ImageFont.truetype('arial.ttf', 36)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor())

# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
