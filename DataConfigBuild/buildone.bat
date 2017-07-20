
@echo off 
::---------------------------------------------------
::参数为xls文件名，不需要后缀
::---------------------------------------------------
for /f "delims=." %%i in (build.txt) do call build_one %%i

echo buid success
@echo on
pause 
