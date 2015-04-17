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

from html.parser import HTMLParser

class Pages(object):
    """Page manager"""
    def __init__(self):
        super(Pages, self).__init__()
        self._page = {}
    def add_page(self,name,url):
        self._page[name]=url
    def del_page(self,name):
        del self_page[name]
    def get_page(self,name):
        return self._page[name]

        

		

#Page handler
class Html_decode(HTMLParser):
	"""Html_decode for the GET"""
	def handle_data(self,data):
		print(data)


class HTMLTableParser(HTMLParser):
    """ Table parser"""
    def __init__(self):
        HTMLParser.__init__(self)
        self._in_td = False
        self._in_th = False
        self._current_table = []
        self._current_row = []
        self._current_cell = []
        self.tables = []

    def handle_starttag(self, tag, attrs):
        """ Parser all tables"""
        if tag == 'td':
            self._in_td = True
        if tag == 'th':
            self._in_th = True

    def handle_data(self, data):
        """ Handle cells"""
        if self._in_td ^ self._in_th:
            self._current_cell.append(data.strip())

    def handle_endtag(self, tag):
        """ Save data"""
        if tag == 'td':
            self._in_td = False
        elif tag == 'th':
            self._in_th = False

        if tag in ['td', 'th']:
            final_cell = " ".join(self._current_cell).strip()
            self._current_row.append(final_cell)
            self._current_cell = []
        elif tag == 'tr':
            self._current_table.append(self._current_row)
            self._current_row = []
        elif tag == 'table':
            self.tables.append(self._current_table)
            self._current_table = []	


def Page_nethandler(opener,singlepage):
    opener.open(singlepage)
    html_doc_data=HTMLTableParser()
    html_doc_data.feed(f.read().decode("gb2312"))
    return html_doc_data.tables