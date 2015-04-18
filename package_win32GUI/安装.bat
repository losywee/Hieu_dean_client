@ECHO OFF&PUSHD %~DP0 &TITLE 安装教务网客户端0.2.1
set "exe=jwc_checker.exe"
set "lnk=教务网辅助客户端"
set "e=Done!"
:Menu
echo a.创建桌面图标
echo 1.仅运行
echo.&echo.
set /p a=输入数字回车：
if "%a%"=="a" Goto DesktopLnk
if "%a%"=="1" Goto RunApp

:RunApp
set "paths=%~dp0\package\%exe%"
echo %paths%
start %paths%

SET E=完成!&GOTO MSGBOX
:AssocProtocol


:DesktopLnk
mshta VBScript:Execute("Set a=CreateObject(""WScript.Shell""):Set b=a.CreateShortcut(a.SpecialFolders(""Desktop"") & ""\%lnk%.lnk""):b.TargetPath=""%~dp0\package\%exe%"":b.WorkingDirectory=""%~dp0"":b.Save:close")&SET E=完成!&GOTO MSGBOX
:MsgBox
if "%1"=="" mshta VBScript:MsgBox("%e%",vbSystemModal,"")(close)& Cls&Goto Menu