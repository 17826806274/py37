# -*- conding:utf-8 -*-
#Author:wzf

from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter.filedialog import askdirectory
import tkinter.filedialog
import os


class StatisticsTool:
    def __init__(self):
        pass

    #调试显示被调用
    def callback(self,text):
        print(text+"被调用")

    #选择文件函数
    def SelectFile(self,FilePath_entry):
        self.default_dir = r"文件路径"
        self.filepath = tk.filedialog.askopenfilename(title='选择文件', initialdir=(os.path.expanduser(self.default_dir)))
        print(self.filepath)
        self.FilePath_entry.delete(0, END)#清空文本框
        self.FilePath_entry.insert(0, self.filepath)

    def selectPath(self):
        # 选择文件path_接收文件地址
        self.path1 = tk.filedialog.askopenfilename()
        self.path.set(self.path1)
        #print(self.path1)

    def savePath(self):
        self.path2 = askdirectory()
        self.savepath.set(self.path2)
        #print(self.savepath)


    def x(self):
        m = [self.path.get(),self.Database_host_text.get(),self.c1.get(),self.c2.get(),self.c3.get()]
        n = {
            'path':self.path.get(),
            'Database_host':self.Database_host_text.get(),
            'Database_username':self.Database_username_text.get(),
            'Database_password':self.Database_password_text.get(),
            'Database_port':self.Database_port_text.get(),
            'Database_database':self.Database_database_text.get(),
            'savepath':self.savepath.get(),
            'c1':self.c1.get(),
            'c2':self.c2.get(),
            'c4':self.c3.get(),
            'c5':self.c5.get(),
            'c6':self.c6.get(),
            'c7':self.c7.get(),
        }
        #self.AA = 'WQEQWEWQE'
        print(n)

    def main(self):
        self.root = Tk()
        self.MainFrame = tk.LabelFrame(self.root,width=400,height=300,text='基础信息',padx=10,pady=10).grid(row =0,column =0,padx = 5)
        self.MainFrame2 = tk.LabelFrame(self.root, width=400, height=300, text='输出选项', padx=10, pady=10).grid(row=0,column=1,padx=5)
        #self.MainFrame3 = tk.LabelFrame(self.root, width=400, height=300, text='输出选项', padx=10, pady=10).grid(row=1,columnspan=2,padx=5)
        #self.root.geometry('1068x681+10+10')

        #创建菜单
        self.menubar = tk.Menu(self.root)
        self.menubar.add_command(label = "设置", command = lambda:self.callback("设置"))
        self.menubar.add_command(label = "帮助", command = lambda:self.callback("帮助"))
        self.root.config(menu = self.menubar)

        #文件选择按键
        self.FileName = tk.Button(self.MainFrame, text="导入Excel", command=self.selectPath).place(x=20,y=20)

        # 文件路径输入框
        self.path = tk.StringVar()
        self.FilePath_entry = tk.Entry(self.MainFrame, textvariable=self.path, width=40).place(x=90,y=25)

        #数据库host
        tk.Label(self.MainFrame, text="host").place(x=20,y=55)
        self.Database_host_text = tk.StringVar()
        tk.Entry(self.MainFrame,textvariable=self.Database_host_text,width = 40).place(x=90,y=55)
        #数据库账号
        tk.Label(self.MainFrame, text="数据库账号").place(x=20,y=85)
        self.Database_username_text = tk.StringVar()
        self.Database_username = tk.Entry(self.MainFrame,textvariable=self.Database_username_text,width = 40).place(x=90,y=85)
        #数据库密码
        tk.Label(self.MainFrame, text="数据库密码").place(x=20,y=110)
        self.Database_password_text = tk.StringVar()
        self.Database_password = tk.Entry(self.MainFrame,textvariable=self.Database_password_text,width = 40,show="*").place(x=90,y=110)
        # 数据库port
        tk.Label(self.MainFrame, text="端口号").place(x=20,y=135)
        self.Database_port_text = tk.StringVar()
        self.Database_port = tk.Entry(self.MainFrame,textvariable=self.Database_port_text, width = 40).place(x=90,y=135)
        #数据库database
        tk.Label(self.MainFrame, text="database").place(x=20,y=160)
        self.Database_database_text = tk.StringVar()
        self.Database_database = tk.Entry(self.MainFrame, textvariable=self.Database_database_text, width = 40).place(x=90,y=160)
        # 文件保存地址
        self.FileSave = tk.Button(self.MainFrame, text="保存目录", command=self.savePath).place(x=20,y=185)
        # 文件路径输入框
        self.savepath = tk.StringVar()
        self.SavePath_entry = tk.Entry(self.MainFrame, textvariable=self.savepath, width=40).place(x=90,y=190)


        #勾选项
        self.c1 = tk.IntVar()
        self.c1.set(1)
        tk.Checkbutton(self.MainFrame, text="通过率", variable=self.c1).place(x=440,y=25)
        self.c2 = tk.IntVar()
        self.c2.set(1)
        y = tk.Checkbutton(self.MainFrame, text="一轮通过率", variable=self.c2).place(x=440,y=60)
        self.c3 = tk.IntVar()
        self.c3.set(1)
        z = tk.Checkbutton(self.MainFrame, text="二轮通过率", variable=self.c3).place(x=440,y=95)
        self.c4 = tk.IntVar()
        self.c4.set(1)
        tk.Checkbutton(self.MainFrame, text="三轮通过率", variable=self.c4).place(x=440,y=130)
        self.c5 = tk.IntVar()
        self.c5.set(1)
        tk.Checkbutton(self.MainFrame, text="预留", variable=self.c5).place(x=440,y=165)
        self.c6 = tk.IntVar()
        self.c6.set(1)
        tk.Checkbutton(self.MainFrame, text="预留",  variable=self.c6).place(x=440, y=200)
        self.c7 = tk.IntVar()
        self.c7.set(1)
        tk.Checkbutton(self.MainFrame, text="预留", variable=self.c7).place(x=440, y=235)

        #生成报表按钮
        tk.Button(self.MainFrame, text="生成报表", command=self.x).place(x=650,y=250)

        self.scr = tk.scrolledtext.ScrolledText(self.MainFrame2, width=35, height=15, font=("隶书", 8)).place(x=550, y=30)

        self.root.mainloop()

if __name__ == '__main__':
    X = StatisticsTool()
    X.main()

