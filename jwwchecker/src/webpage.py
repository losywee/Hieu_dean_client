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

#All pages i known
had_known_page=[
'LOGIN=http://222.247.62.198/jiaowu/Login.aspx',
#Cet result
'CET=http://222.247.62.198/jiaowu/JWXS/kjbm/Jwxs_Kjbm_list.aspx',
#Exam grade
'S_G=http://222.247.62.198/jiaowu/JWXS/cjcx/jwxs_cjcx_like.aspx',
#Personal material
'X_J=http://222.247.62.198/jiaowu/JWXS/xskp/jwxs_xskp_like.aspx',
#Lesson array
'K_B=http://222.247.62.198/jiaowu/JWXS/pkgl/XsKB_List.aspx',
#evaluate teacher
'H_P=http://222.247.62.198/jiaowu/JWXS/Default.aspx',
#考试安排
'E_P=http://222.247.62.198/jiaowu/JWXS/ksap/jwxs_ksap_like.aspx',
#教师评估
'J_T=http://222.247.62.198/jiaowu/JWXS/JSPG/JWXS_JSPG_MENU.aspx',
#毕业管理 http://222.247.62.198/jiaowu/JWXS/BYGL/JWXS_BYGL_LIST.aspx
'G_M=http://222.247.62.198/jiaowu/JWXS/BYGL/JWXS_BYGL_LIST.aspx',
#重修安排 http://222.247.62.198/jiaowu/JWXS/CJBM/XSBM_BKBM_LIST1.ASPX
'R_S=http://222.247.62.198/jiaowu/JWXS/CJBM/XSBM_BKBM_LIST1.ASPX',
#课表调整 http://222.247.62.198/jiaowu/JWXS/PKGL/JWXS_XSTTKCX_LIST.aspx
'T_A=http://222.247.62.198/jiaowu/JWXS/PKGL/JWXS_XSTTKCX_LIST.aspx',
#选课 http://222.247.62.198/jiaowu/JWXS/xsxk/XSXK_MENU.aspx
'S_C=http://222.247.62.198/jiaowu/JWXS/xsxk/XSXK_MENU.aspx',
#补考 http://222.247.62.198/jiaowu/JWXS/CJBM/XSBM_BKBM_LIST.aspx
'R_T=http://222.247.62.198/jiaowu/JWXS/CJBM/XSBM_BKBM_LIST.aspx',
#教学计划 http://222.247.62.198/jiaowu/JWXS/jxjh/jwxs_jxjh_list.aspx
'T_P=http://222.247.62.198/jiaowu/JWXS/jxjh/jwxs_jxjh_list.aspx',
#预警 http://222.247.62.198/jiaowu/JWXS/PKGL/JWXS_XSXJYJXX_FIND.aspx
'ALARM=http://222.247.62.198/jiaowu/JWXS/PKGL/JWXS_XSXJYJXX_FIND.aspx',
#Checkcode
'CODE_PAGE=http://222.247.62.198/jiaowu/other/CheckCode.aspx?datetime=az'
]

unknow_page=[]