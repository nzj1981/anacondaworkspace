# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_psutil_mem.py 
@time: 2018/3/27 16:52
"""

'''
通过psutil获取系统内存信息
'''

import psutil

print('获取内存信息及交换内存信息')
print(psutil.virtual_memory())
print(psutil.swap_memory())

print('获取磁盘信息:')
print('磁盘分区信息:')
print(psutil.disk_partitions())
print('磁盘使用信息:')
print(psutil.disk_usage('c:'))
print('磁盘IO:')
print(psutil.disk_io_counters())
