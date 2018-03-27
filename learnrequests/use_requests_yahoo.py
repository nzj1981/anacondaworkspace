# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: use_requests_yahoo.py 
@time: 2018/3/26 16:37
"""

'''
利用requests第三方组件请求雅虎搜索
'''

import requests

sea_text = '库库'
r = requests.get('https://search.yahoo.com/search',
                 params={'p': sea_text, 'fr': 'yfp-t', 'fp': 1,
                         'toggle': 1, 'cop': 'mss', 'ei': 'UTF-8'})
print('连接状态码')
print(r.status_code)
print('输出连接地址')
print(r.url)
print('检测编码')
print(r.encoding)
print('获得byytes对象')
print(r.content)

print("直接获得JSON格式****************************************************")
r1 = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print('输出JSON格式')
print(r1.json())

print('需要传入HTTP Header时,我们传入一个dict作为headers参数')
r2 = requests.get('https://www.douban.com', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
# print(r2.text)
print(r2.headers, r2.headers['Content-Type'])

print('****发送POST请求-数据参数可以为表单id或表单name****')
r3 = requests.post('https://accounts.douban.com/login', headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'},
                   data={'email': '13283818083@126.com', 'password': '***'})
print(r3.status_code)

'''
requests默认使用application/x-www-form-urlencoded对POST数据编码.
如果要传递JSON数据,可以直接传入json参数:
params = {'key': 'value'}
r = requests.post(url, json=params) #内部自动序列化为JSON
requests可以把上传文件需要更复杂编码格式给简化成files参数:
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
注:在读取文件时,注意务必使用'rb'的二进制模式读取,这样获取的
bytes长度才是文件的长度.
'''
print('*********设置cookies*************')

cs = {'token': '12345', 'status': 'working'}
url = 'https://www.douban.com'
r4 = requests.get(url, cookies=cs)
print(r4.status_code, r4.cookies)
