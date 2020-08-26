# -*- conding:utf-8 -*-
#Author:wzf
import tkinter.filedialog
import tkinter as tk
from tkinter import *
from flask import Flask



def selectPath():
    # 选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()
    path.set(path_)
    print(path_)

main_box = tk.Tk()
#变量path
path = tk.StringVar()
#输入框，标记，按键
tk.Label(main_box,text = "目标路径:").grid(row = 0, column = 0)
#输入框绑定变量path
tk.Entry(main_box, textvariable = path).grid(row = 0, column = 1)
tk.Button(main_box, text = "路径选择", command = selectPath).grid(row = 0, column = 2)
main_box.mainloop()







