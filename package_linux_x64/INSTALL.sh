 
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

BINARY_PATH=""
BINARY_NAME="jwc_checker"
INSTALL_PATH="/opt"
# Check if user is root
check_user() {
	if [ $(id -u) != "0" ]; then
    	echo "Error: You must be root to run this script, please use root to install jwc_checker"
    	exit 1
	fi
}

#Check system
system_check() {

	OS_BIT=$(getconf LONG_BIT)
	if [[ $OS_BIT == 64 ]]; then
		return 0
	else
		echo "Must be x64 OS."
		exit 1
	fi

}

print_hello() {
	echo "========================================================================="
	echo "Jwc checker V0.2.1 for Linux x64, Written by anchowee@163.com"
	echo "========================================================================="
	echo "Author:anchowee !@@@@#$%"
	echo "QQ:529238084"
	echo "For more information please visit https://www.5di.us"
	echo "========================================================================="
}

begin_setup() {
	chmod +777 jwc_checker_x64
	cp -R "jwc_checker_x64" $INSTALL_PATH
	cp "$INSTALL_PATH/jwc_checker_x64/res/swjwc.desktop" "/usr/local/share/applications/"
	echo "install finised!"
	echo "Please run: $INSTALL_PATH/jwc_checker_x64/$BINARY_NAME "
	

}

main() {
	check_user
	print_hello
	system_check
	begin_setup
}

main