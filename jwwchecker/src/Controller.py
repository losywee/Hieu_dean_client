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

import webpage
import networkhandler
import login_handler
import utils
import urllib.request

#Pages decode.
def Handle_allpages():
	page_saver=networkhandler.Pages()
	try:
		all_pages=webpage.had_known_page
		num_page=len(all_pages)
		print(num_page)
		for page in range(num_page):
			split_page=all_pages[page]
			page_index=split_page.split("=")
			page_saver.add_page(page_index[0],page_index[1])
	except:
		print("Unknown page_handler error.")
		raise
	return page_saver
#Get checkcode	
def Get_checkcode(page_saver):
	checkcode=login_handler.Web_login()
	ck_state=checkcode.jpg_request(page_saver.get_page('LOGIN'),page_saver.get_page('CODE_PAGE'))
	jpg_state=login_handler.Login_state()
	jpg_state.set_state(ck_state)

#Login jwc
def Begin_login(page_saver,userinfo,checkcode):
	params=login_handler.Web_login()
	params.set_userinfo(userinfo)
	currentpar=params.encode_params(checkcode)
	req = urllib.request.Request(page_saver.get_page('LOGIN'),currentpar,utils.REQUEST_HEADER,method="POST")
	currentstat=login_handler.Login_state()
	sates_login=currentstat.get_state()
	try:
		f=sates_login.open(req)
		f=sates_login.open(page_saver.get_page('H_P'))
		currentstat.set_state(sates_login)
		html_doc_data= networkhandler.HTMLTableParser()
		html_doc_data.feed(f.read().decode("gb2312"))
		return html_doc_data.tables
	except:
		print('Login failure,Unknown')
		raise
#handler for all pages	
def Page_tablize(page_saver,page_index):
	stat=login_handler.Login_state()
	currentstat=stat.get_state()
	try:
		f=currentstat.open(page_saver.get_page(str(page_index)))
		html_doc_data= networkhandler.HTMLTableParser()
		html_doc_data.feed(f.read().decode("gb2312"))
		#currentstat.set_state(currentstat)
		return html_doc_data.tables
	except:
		print('Page_tablize failure.')
		raise
	
	
	
	







	

