@ECHO OFF&PUSHD %~DP0 &TITLE ��װ�������ͻ���0.2.1
set "exe=jwc_checker.exe"
set "lnk=�����������ͻ���"
set "e=Done!"
:Menu
echo a.��������ͼ��
echo 1.������
echo.&echo.
set /p a=�������ֻس���
if "%a%"=="a" Goto DesktopLnk
if "%a%"=="1" Goto RunApp

:RunApp
set "paths=%~dp0\package\%exe%"
echo %paths%
start %paths%

SET E=���!&GOTO MSGBOX
:AssocProtocol


:DesktopLnk
mshta VBScript:Execute("Set a=CreateObject(""WScript.Shell""):Set b=a.CreateShortcut(a.SpecialFolders(""Desktop"") & ""\%lnk%.lnk""):b.TargetPath=""%~dp0\package\%exe%"":b.WorkingDirectory=""%~dp0"":b.Save:close")&SET E=���!&GOTO MSGBOX
:MsgBox
if "%1"=="" mshta VBScript:MsgBox("%e%",vbSystemModal,"")(close)& Cls&Goto Menu