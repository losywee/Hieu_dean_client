 
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

BINARY_PATH="/usr/local/share/losyweeapp/jwwchecker/src/"

# Check if user is root
check_user() {
	if [ $(id -u) != "0" ]; then
    	echo "Error: You must be root to run this script, please use root to install jwc_checker"
    	exit 1
	fi
}

print_hello() {
	echo "========================================================================="
	echo "Jwc checker V0.2.1 for Linux "
	echo "========================================================================="
	echo "Author:anchowee !@@@@#$%"
	echo "QQ:529238084"
	echo "For more information please visit https://www.5di.us"
	echo "========================================================================="
}

main() {

print_hello
check_user
ln -s $BINARY_PATH/jwwclient.py /usr/bin/jwwclient
echo 'Install finished! Please run in terminal with jwwclient.'
echo 'usage:   jwwclient'


}

main