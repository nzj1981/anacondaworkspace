# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_pil_resize.py 
@time: 2018/3/26 14:29
"""

'''
利用pil库修改图片大小
'''

from PIL import Image, ImageFilter

# 打开一个jpg图像文件,注意是当前路径
im = Image.open('test.jpg')

# 获得图像尺寸
w, h = im.size
print('Original image size:{}x{}'.format(w, h))

# 缩放到50%,注意缩略图是两个小括号
im.thumbnail((w // 2, h // 2))
print('Resize image to:{}x{}'.format(w // 2, h // 2))

# 把缩放后的图像用jpg格式保存
im.save('thumbnail.jpg', 'jpeg')

# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')

