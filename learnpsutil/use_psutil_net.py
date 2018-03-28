# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_psutil_net.py 
@time: 2018/3/28 10:22
"""

'''
psutil获取网络接口和网络连接信息
'''

import psutil

print('获取网络读写字节/包的个数')
print(psutil.net_io_counters())

print('获取网络接口信息')
print(psutil.net_if_addrs())

print('获取网络接口状态')
print(psutil.net_if_stats())

print('获取当前网络连接信息,或启用root权限')
print(psutil.net_connections())
