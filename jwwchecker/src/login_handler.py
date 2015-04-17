#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.cookiejar
import urllib.request
import urllib.parse
from html.parser import HTMLParser
import utils

#@parm website_address userinfo
class User_info(object):
	'''A userinfo consist of password and name.'''
	def __init__(self, parm):
		super(User_info, self).__init__()
		self.parm=parm
		self.username = parm['username']
		self.password=parm['password']
	def get_username(self):
		return self.username
	def get_userpassword(self):
		return self.password
		

class Web_login(object):
	'''Login the jwc.hieu.cn'''
	def __init__(self):
		super(Web_login, self).__init__()
	def set_userinfo(self,obj_userinfo):
		userinfo=User_info(obj_userinfo)
		self.username = userinfo.get_username()
		self.password=userinfo.get_userpassword()
	def __cookies_im(self,resurl):
		try:
			REQUEST_URL=resurl
			cj = http.cookiejar.CookieJar()
			opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
			#Start request
			urllib.request.install_opener(opener)
			requests=opener.open(REQUEST_URL)
			return opener
		except e:
			raise e		
	def encode_params(self,checkcode):
		
		code=checkcode
		params=urllib.parse.urlencode({
			'PWD':self.password,"__VIEWSTATE":"/wEPDwULLTE1OTUyMTE3MDAPZBYCAgMPZBYEAg8PDxYCHgRUZXh0ZWRkAhEPDxYCHwAFAjM3ZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFB0Noa1VzZXLGfvzkkht9e41y+IWC4Mj1YTaDBw==",
			"__EVENTVALIDATION":"/wEWBwKGhfPoDwKvo8HwCwKG85bvBgLO44u1DQLAiqigBwLM6LcMApnA7cMNidQjrHntebffq3Vuq2RIxxGPJi0=",
			'Account':self.username,'CheckCode':code,'cmdok':''})
		params=params.encode('gb2312')
		return params
	def jpg_request(self,requrl,codeurl):
		try:
			opener=self.__cookies_im(requrl)
			req =  opener.open(codeurl)
			img=req.read()
			open(utils.get_tempfile('code.jpg'), 'wb').write(img)
			return opener
		except:
			print("login_handler request jpg error,status:Unknown")
			raise


#Login state handler		
class Save_state:
	"""Save state"""
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

class Login_state(Save_state):
	"""Login_state"""
	def __init__(self,):
		super(Login_state, self).__init__()

	def get_state(self):
		return self.__login_state
	def set_state(self,state):
		self.__login_state=state
		return self.__login_state
		
						
	
