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
import os
import codever
import utils
from PIL import Image,ImageTk
import Model
import mainframe

class Login(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)
        #Model   
        self.loginmodel=Model.Page_dataphraser()
        self.loginmodel.get_checkcode()
        self.HAD_AUTH=0

        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        self.get_config()


        self.parent.title("教务网登录客户端")
        self.style = Style()
        self.style.theme_use("alt")
        self.style.configure(self.parent,background="#16a085")
        self.style.configure("BW.TLabel", foreground="black", background="white",anchor="center",expand=1)
        self.style.configure("BW.TFrame", foreground="white", background="white",anchor="center",expand=1)
        self.style.configure("BW.TButton", foreground="green", background="#34495e",padding=(0, 5, 0, 5))
        frame = Frame(self, relief=RAISED, borderwidth=1,style="BW.TFrame",width=300,height=200)
        lb_usn=Label(frame,text="用户名:", style="BW.TLabel").grid(row=0,padx=20,pady=15)
        lb_pwd=Label(frame,text="密码:", style="BW.TLabel").grid(row=1,padx=20,pady=15)
        lb_code=Label(frame,text="验证码:", style="BW.TLabel").grid(row=2,padx=20,pady=15)
        self.usn_entry=Entry(frame)
        self.pwd_entry=Entry(frame)
        self.code_entry=Entry(frame)
        self.usn_entry.grid(row=0,column=1,sticky=E)
        self.pwd_entry.grid(row=1,column=1,sticky=E)
        self.code_entry.grid(row=2,column=1,sticky=E)
        frame.pack(fill=BOTH, expand=1)        
        self.pack(fill=BOTH, expand=1)        
        closeButton = Button(self, text="退出",command=self.close_window,style="BW.TButton")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="登录",style="BW.TButton",command=self.dologin)
        okButton.pack(side=RIGHT)
        canvas = Canvas(self, width=70, height=23)
        canvas.pack(side=LEFT,padx=4)


        img_file = Image.open(utils.get_tempfile("code.jpg"))
        canvas.image = ImageTk.PhotoImage(img_file)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')


        self.usn_entry.insert(0,self.username)
        self.pwd_entry.insert(0,self.password)
    def dologin(self):

        self.username=str(self.usn_entry.get())
        self.password=str(self.pwd_entry.get())
        self.checkcode=str(self.code_entry.get())
        if self.username.isdigit():
            pass
        else:
            self.usn_entry.delete(0, END)
            self.usn_entry.insert(0,"帐号格式不正确！")
            self.HAD_AUTH=0
            return

        if len(self.password)==0:
            self.pwd_entry.delete(0, END)
            self.pwd_entry.insert(0,"请正确输入密码！")
            self.HAD_AUTH=0
            return
        elif len(self.checkcode)==0:
            self.code_entry.delete(0, END)
            self.code_entry.insert(0,"请根据下图所示的验证码进行输入")
            utils.HAD_AUTH=0
            return 
        elif len(self.username)==0:
            self.HAD_AUTH=0
            return
        user_name=self.username
        user_pwd=self.password
        utils.userinfo["username"]=self.username
        utils.userinfo["password"]=self.password
        self.set_config()
        self.login_data=self.loginmodel.login_website(utils.userinfo,self.checkcode)
        self.HAD_AUTH=1
        self.close_window()
        
    def get_config(self):
        config=utils.Configfile(utils.userinfo,"")
        self.username=config.get_username()
        self.password=config.get_password()
    def set_config(self):
        config=utils.Configfile(utils.userinfo,"")
        config.write_username_passwd()
    def close_window(self):
        self.parent.destroy()


        


                                                                    


    
