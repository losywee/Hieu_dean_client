#!/bin/sh
# Copyright (C) 2015 Losywee.
# Accelbo Group              
#
# Author:     Losywee <anchowee@mmda.info>
# Maintainer: Losywee <anchowee@mmda.info>
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
LIBDIR = $(DESTDIR)/usr/local/share/losyweeapp
BINDIR = $(DESTDIR)/usr/bin/

clean:
	rm -f *.py[co] */*.py[co]
install:
	echo "Welcome to install the application."
	mkdir -p $(LIBDIR)
	mkdir -p $(BINDIR)
	cp -R jwwchecker $(LIBDIR)
	echo "Install finished,Please commandline run: Install.sh"
uninstall:
	echo "Uninstall"
	rm -rf $(LIBDIR)/jwwchecker
	rm -rf /usr/bin/jwwclient
	echo "Uninstall finished."


