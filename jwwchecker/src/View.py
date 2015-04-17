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

from  loginframe import *
from mainframe import *

class Ui_switcher(object):
	"""Select a ui"""
	def __init__(self):
		super(Ui_switcher, self).__init__()
		self.loginui = ""
		self.mainui=""
	def switch_ui(self,ui,x_size,y_size):
		root = Tk()
		
		w=root.winfo_screenwidth()
		h=root.winfo_screenheight()
		root.geometry("%dx%d+%d+%d" % (x_size,y_size, (w-x_size)/2, (h-y_size)/2 ))
		if ui=='login':
			#root.overrideredirect(1)
			root.resizable(width=FALSE, height=FALSE)
			self.loginui=Login(root)
			self.current_ui='login'
		elif ui=='main':
			self.mainui=Check_frame(root)
			self.current_ui='main'

		root.mainloop()
	def close_ui(self,args):
		if args=='login':
			self.loginui.close_window()
			return 0
		elif args=='main':
			self.mainui.close_window()
			return 0
	def login_status(self):
		if self.loginui.HAD_AUTH==1:
			self.switch_ui('main',800,500)





