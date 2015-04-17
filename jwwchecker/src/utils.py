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

import configparser
import os.path
import tempfile
from os.path import expanduser
import codever

userinfo={'username':'','password':''}
checkcode=''
CONFIGFILE=expanduser("~")+'/set.ini'
HAD_AUTH=0


def get_tempfile(fname):
	tdir=tempfile.gettempdir()
	tempfiledir=str(tdir)+"/"+str(fname)
	return tempfiledir

#request header
REQUEST_HEADER = {
                    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',
                    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'accept-language':'zh-CN,zh;q=0.8',
                    'connection':'keep-alive',
                    'content-type':'application/x-www-form-urlencoded',
                    'Referer':'http://222.247.62.198/jiaowu/Login.aspx'

        }


class Configfile(object):
	"""Doc files"""
	def __init__(self, userinfo,netmode=0):
		super(Configfile, self).__init__()
		self.username = userinfo["username"]
		self.password = userinfo["password"]
		self.netmode = '默认外网模式'
		config = configparser.ConfigParser()
		if os.path.isfile(CONFIGFILE):
			pass
		else:
			f=open(CONFIGFILE,"w+")
			config["default"]={'username':'test','password':'test','developer':'anchowee@163.com','netmode':0}
			config.write(f)
			f.close()

	def get_username(self):
		config = configparser.ConfigParser()
		config.read(CONFIGFILE)
		if 'default' in config:
			return config['default']['username']

		else:
			return False
	def get_password(self):
		config = configparser.ConfigParser()
		config.read(CONFIGFILE)
		if 'default' in config:
			return config['default']['password']
		else:
			return False
	def get_netmode(self):
		config = configparser.ConfigParser()
		config.read(CONFIGFILE)
		if 'default' in config:
			return config['default']['netmode']
		else:
			return False
		pass
	def write_username_passwd(self):
		config = configparser.RawConfigParser()
		config.add_section('default')
		config.set('default','username',self.username)
		config.set('default','password',self.password)
		config.set('default','netmode',self.netmode)
		config.set('default','当前版本',codever.CX_VER)
		config.set('default','联系作者QQ：',codever.QQ)
		config.set('default','程序编译环境：',codever.Build_System)
		with open(CONFIGFILE, 'w') as configfile:
			config.write(configfile)


