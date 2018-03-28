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
通过psutil获取系统内存、磁盘信息
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

# ***************获取进程信息************************

print('打印所有进程ID')
print(psutil.pids())

print('获取指定进程ID=6780')
print(psutil.Process(6780))

ps = psutil.Process(6780)

print('\n进程名称: %s' % ps.name())
print('\n进程exe路径: %s' % ps.exe())
print('\n进程工作目录: %s' % ps.cwd())
print('\n进程启动命令行: %s' % ps.cmdline())
print('\n父进程ID: %s' % ps.ppid())
print('\n父进程: %s' % ps.parent())
print('\n子进程列表: %s' % ps.children())
print('\n进程创建时间: %s' % ps.create_time())
print('\n进程状态: %s' % ps.status())
print('\n进程用户名: %s' % ps.username())
print('\n进程使用CPU时间: %s' % ps.cpu_times)
print('\n进程使用的内存: %s' % ps.memory_info)
print('\n进程相关网络连接: %s' % ps.connections())
print('\n进程的线程数量: %s' % ps.num_threads())
print('\n所有的线程信息: %s' % ps.threads())
print('\n进程环境变量: %s' % ps.environ())


# print('\n结束进程: %s' % ps.terminate())
'''
test()函数，可以模拟出ps命令的效果：
'''

print('\n模拟ps命令')
psutil.test()



