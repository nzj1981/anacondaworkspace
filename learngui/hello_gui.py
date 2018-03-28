# encoding: utf-8
""" 
@version: v1.0 
@author: autumner 
@license: Apache Licence  
@contact: 18322313385@163.com 
@site: https://github.com/nzj1981/anacondaworkspace.git 
@software: PyCharm 
@file: hello_gui.py 
@time: 2018/3/28 20:44
"""
'''
Python支持多种图形界面的第三方库：
Tk
wxWidgets
Qt
GTK
其中Tk是python自带的库，使用Tkinter无需安装任何包。
'''
# 导入Tkinter包的所有内容
from tkinter import *


# 从Frame派生一个Application类,这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


'''
pack()方法把Widget加入到父容器中,并实现布局.
pack()是最简单的布局,grid()可以实现更复杂的布局
在createWidgets()方法中,我们创建一个Label和一个Button,当
Button被点击时,触发self.quit()使程序退出
'''

# 实例化Application,并启动消息循环
app = Application()
# 设置窗口标题
app.master.title('Hello world')
# 主消息循环
app.mainloop()
