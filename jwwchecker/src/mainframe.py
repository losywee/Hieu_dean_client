#!/usr/bin/env python
# coding=utf-8

# Copyright (C) 2015 anchowee@163.com.
#               
#
# Author:     Losywee <Losywee@gmail.com>
# Maintainer: Losywee <Losywee@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import codever
import Model

#self.hide()
class Check_frame(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        #Model   
        self.mainmodel=Model.Page_dataphraser() 
        self.parent = parent
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("教务网查询辅助客户端")
        self.style = Style()
        self.style.theme_use("clam")
        self.style.configure(self.parent,background="#ECF0F1")
        self.style.configure("BW.TLabel", foreground="black", background="white",anchor="center",expand=1)
        self.style.configure("BW.TFrame", foreground="black", background="white",anchor="center",expand=1)
        self.style.configure("BW.TButton", foreground="#2C3E50", background="#E74C3C",padding=(0, 4, 0, 4))
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        #self.columnconfigure(3, pad=1)
        self.rowconfigure(3, weight=1)
        #self.rowconfigure(5, pad=2)
        #self.rowconfigure(5, weight=1)
        #self.rowconfigure(7, pad=2)
        #self.rowconfigure(7, weight=1)
        #self.rowconfigure(9, pad=2)
        self.lbv = StringVar()
        self.lbl = Label(self, textvariable=self.lbv,style="BW.TLabel")
        self.lbv.set("点击你需要查询的功能！")
        self.lbl.grid(sticky=W, pady=4, padx=5)

        
        self.area = Text(self)
        self.area.grid(row=1, column=0, columnspan=2, rowspan=8, 
            padx=5, sticky=E+W+S+N)
        
        abtn = Button(self, text="查询课表",style="BW.TButton",command=lambda:self.handle_cmd('K_B'))
        abtn.grid(row=1, column=3,pady=2)
        abtn8 = Button(self, text="课表调整",style="BW.TButton",command=lambda:self.handle_cmd('T_A'))
        abtn8.grid(row=1, column=4,pady=2)
        

        cbtn_xueji = Button(self, text="查询学籍",style="BW.TButton",command=lambda:self.handle_cmd('X_J'))
        cbtn_xueji.grid(row=2, column=3,pady=2)

        abtn_xgcji = Button(self, text="四六级查询",style="BW.TButton",command=lambda:self.handle_cmd('CET'))
        abtn_xgcji.grid(row=3, column=3,pady=2)
        abtn_chengji = Button(self, text="查询成绩",style="BW.TButton",command=lambda:self.handle_cmd('S_G'))
        abtn_chengji.grid(row=3, column=4, pady=2)

        abtn5 = Button(self, text="选课",style="BW.TButton",command=lambda:self.handle_cmd('S_C'))
        abtn5.grid(row=4, column=3,pady=2)
        
        abtn6 = Button(self, text="补考",style="BW.TButton",command=lambda:self.handle_cmd('R_T'))
        abtn6.grid(row=5, column=3,pady=2)
        abtn2 = Button(self, text="考试安排",style="BW.TButton",command=lambda:self.handle_cmd('E_P'))
        abtn2.grid(row=5, column=4,pady=2)

        abtn1 = Button(self, text="教师评估",style="BW.TButton",command=lambda:self.handle_cmd('J_T'))
        abtn1.grid(row=6, column=3,pady=2)
        abtn4 = Button(self, text="重修安排",style="BW.TButton",command=lambda:self.handle_cmd('R_S'))
        abtn4.grid(row=6, column=4,pady=2)
        
        abtn3 = Button(self, text="毕业管理",style="BW.TButton",command=lambda:self.handle_cmd('G_M'))
        abtn3.grid(row=7, column=3,pady=2)
        
        abtn7 = Button(self, text="预警",style="BW.TButton",command=lambda:self.handle_cmd('ALARM'))
        abtn7.grid(row=7, column=4,pady=2)

        
        hbtn_help = Button(self, text="帮助",style="BW.TButton",command=self.open_help)
        hbtn_help.grid(row=9, column=0, padx=5)
        obtn_qiangke = Button(self, text="退出",style="BW.TButton",command=self.close_window)
        obtn_qiangke.grid(row=9, column=4,pady=2)

        self.Init_data()
        
    def open_help(self):
        messagebox.showinfo("关于本程序","\
            Ver:"+codever.CX_VER+"\n本程序基于GPL协议开放源代码，\n获取源代码联系：anchowee@163.com\n兼容操作系统\
            ：\nWindows/Linux/Android/Mac osx/Ubuntu/国产操作系统等等！\n具体可以参考Python兼容的操作系统。\n"+\
            "Author:"+codever.AUTHOR+"\nWebsite:"+codever.AUTHOR_WEBSITE)

    def close_window(self):
        self.parent.destroy()
    def handle_cmd(self,cmd):
        
        data_len=0
        cached_db=""
        tb_data=""
        try:
            self.area.delete(1.0, END)
        except e:
            raise e
        if self.mainmodel.had_cached(cmd):
            cached_db=self.mainmodel.get_cachedata(cmd)
            tb_data=self.mainmodel.tb_phraser(cached_db,cmd)
            data_len=len(tb_data)
        else:
            tb_data=self.mainmodel.handler_cmd(cmd)
            tb_data=self.mainmodel.tb_phraser(tb_data,cmd)
            data_len=len(tb_data)
        self.currentdata=tb_data
        for x in range(data_len):
            for y in tb_data[x]:
                self.area.insert(INSERT, "\n","n")
                for z in y:
                    self.area.insert(INSERT, "----","n")
                    self.area.insert(INSERT, str(z),"n")
                    self.lbv.set('查询完成！')
    def Init_data(self):
        self.handle_cmd('H_P')
        default_data=self.currentdata
        for x in default_data[0]:
            self.lbv.set(x[2])


