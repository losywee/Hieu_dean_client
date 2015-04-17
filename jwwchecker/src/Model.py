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

import Controller
#Page data handler and cache handler,then controller
class Page_dataphraser(object):
	"""The Page_data_phraser"""
	__request_cache={}
	def __init__(self):
		super(Page_dataphraser, self).__init__()
		self.__dict__=self.__request_cache
		self.page_saver=Controller.Handle_allpages()
	#tables from 
	def tb_phraser(self,tables_data,token):
		if(token not in self.__request_cache):
			try:
				self.__request_cache[str(token)]=tables_data
				return tables_data
			except:
				print('tb_phraser cache error')
				raise

		
		tb_data=tables_data
		return tb_data
	def get_cachedata(self,token):
		cached_data=self.__request_cache[str(token)]

		return cached_data

	def had_cached(self,token):
		if(token not in self.__request_cache):
				return False

		return True
	def get_checkcode(self):
		Controller.Get_checkcode(self.page_saver)
	def login_website(self,userinfo,checkcode):
		return Controller.Begin_login(self.page_saver,userinfo,checkcode)
	def handler_cmd(self,page_index):
		return Controller.Page_tablize(self.page_saver,page_index)


		
		






		
