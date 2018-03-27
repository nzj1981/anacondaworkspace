# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_psutil_cpu.py 
@time: 2018/3/27 16:40
"""

'''
psutil第三方库，主要用于运维工作使用。
psutil=process and system utilities
可以通过一两行代码实现系统监控，更可以跨平台使用。
'''

import psutil

print('CPU逻辑数量：', psutil.cpu_count())
print('CPU物理核心：', psutil.cpu_count(logical=False))
print('统计CPU的用户/系统/空闲时间：', psutil.cpu_times())
print('实现类似top命令的CPU使用率,每秒刷新一次,累计10次')
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))