#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Author: whtrys
Email: whtrys@163.com
Description:
"""
import os.path

from ttkbootstrap import Style
import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkms
import json
import main

open_time = 0


class Main(main.Main):
    def __init__(self):
        super().main_path
        self.child_window = None
        self.main_window = None
        self.main_json = None
        self.save_path = None
        self.main()

    def freeze_main_window(self):
        """
        冻结窗口
        :return:
        """
        self.main_window.attributes("-disabled", 1)

    def free_main_window(self):
        """
        释放被冻结的窗口
        :return:
        """
        self.main_window.attributes("-disabled", 0)

    def open_directory(self):
        self.save_path = tkfd.askdirectory()

        try:
            self.child_window.destroy()
        except:
            pass
        else:
            pass

        self.free_main_window()
        save_json = {"last_save_path": self.save_path}
        json_type = json.dumps(save_json)
        with open("{}\\save.json".format(self.main_path), 'w') as j:
            j.write(json_type)

    def create_project(self):
        self.open_directory()
        about_json = {"subject": ['']}
        json_type = json.dumps(about_json)
        with open("{}\\about.json".format(self.main_path), 'w') as j:
            j.write(json_type)

    def make_child_window(self):
        """
        创建子窗口以用来询问打开还是新建
        :return:
        """

        self.child_window = tk.Toplevel(self.main_window)  # 生成子窗口，可以加入到事件中触发
        self.child_window.overrideredirect(True)
        self.child_window.geometry("200x200+500+500")
        self.child_window.attributes("-topmost", 1)
        tk.Label(self.child_window, text="")

        if self.first_open:
            self.freeze_main_window()
            os.mkdir('{}\\TestManager'.format(self.doc_path))

            tk.Button(self.child_window, text="冻结", command=self.freeze_main_window).pack()
            tk.Button(self.child_window, text="解除", command=self.free_main_window).pack()

            # tk.Button(self.child_window, text="打开", command=self.open_directory).grid(row=0, column=0)
            # tk.Button(self.child_window, text="新建", command=self.free_main_window).grid(row=0, column=1)
            # tk.Button(self.child_window, text="关闭", command=self.main_window.destroy).grid(row=0, column=2)

        else:
            pass
        self.child_window.mainloop()

    def main(self):
        global open_time

        open_time += 1
        style = Style(theme='yeti')

        self.main_window = style.master
        self.main_window.title("TestManager")
        self.main_window.geometry('800x600')

        # self.main_path = tkfd.askdirectory()
        # self.main_json = json.

        # 菜单
        menu_bar = tk.Menu(self.main_window)

        file_menu = tk.Menu(menu_bar, tearoff=False)
        file_menu.add_command(label="打开", command=Main)
        file_menu.add_command(label="保存", command='')
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.main_window.quit)
        menu_bar.add_cascade(label="文件", menu=file_menu)

        menu_bar.add_command(label="设置", command='')

        tk.Label(self.main_window, text=self.main_path)

        self.main_window.config(menu=menu_bar)

        self.make_child_window()

        self.main_window.mainloop()


if __name__ == '__main__':
    Main()
