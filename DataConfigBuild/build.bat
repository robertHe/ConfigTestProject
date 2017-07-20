
@echo off 
set TEMP=temp
::---------------------------------------------------
::参数为xls文件名，不需要后缀
::---------------------------------------------------

if exist %TEMP% rd /s/q %TEMP%
md %TEMP%
for /f "delims=." %%i in (build.txt) do copy DataConfig\%%i.xlsx %TEMP%

call build_folder %TEMP%
rd /s/q %TEMP%
echo buid success
@echo on
pause 
