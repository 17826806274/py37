# -*- conding:utf-8 -*-
#Author:wzf
import tkinter as tk
from tkinter import filedialog
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.filePath = tk.StringVar()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 获取文件
        self.getFile_bt = tk.Button(self)
        self.getFile_bt['width'] = 15
        self.getFile_bt['height'] = 1
        self.getFile_bt["text"] = "打开"
        self.getFile_bt["command"] = self._getFile
        self.getFile_bt.pack(side="top")

        # 显示文件路径
        self.filePath_en = tk.Entry(self, width=30)
        self.filePath_en.pack(side="top")

        self.filePath_en.delete(0, "end")
        self.filePath_en.insert(0, "请选择文件")

    # 打开文件并显示路径
    def _getFile(self):
        default_dir = r"文件路径"
        self.filePath = tk.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        print(self.filePath)
        self.filePath_en.delete(0, "end")
        self.filePath_en.insert(0, self.filePath)


root = tk.Tk()
root.title("Demo")
root.geometry("500x300+600+300")

app = Application(master=root)
app.mainloop()
