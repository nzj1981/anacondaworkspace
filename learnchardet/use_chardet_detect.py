# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_chardet_detect.py 
@time: 2018/3/27 16:26
"""

'''
chardet第三方库,是用来检测字符串编码的,非常简单易用
'''

import chardet

cha = chardet.detect(b'Hello, world!')
print('检测ascii\n', cha)
'''
{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
encoding:用什么编码,
confidence:检测的概率是1.0即100%
language:代表什么语言
'''
data = '离离原上草,一岁一枯荣'.encode('gbk')
print('检测中文\n', chardet.detect(data))

data1 = '离离原上草,一岁一枯荣'.encode('utf-8')
print('检测utf-8\n', chardet.detect(data1))
data2 = '最新の主要ニュース'.encode('euc-jp')
print('检测日文\n', chardet.detect(data2))