
@echo off

set FOLDER_NAME=%1
set DATA_DEST=%2



echo.
echo =========Compilation of %FOLDER_NAME%=========


::---------------------------------------------------
::第一步，将xls经过xls_deploy_tool转成data和proto
::---------------------------------------------------
set STEP1_XLS2PROTO_PATH=step1_xls2proto

@echo on
cd %STEP1_XLS2PROTO_PATH%

::@echo off
::echo TRY TO DELETE TEMP FILES:
::del *_pb2.py
::del *_pb2.pyc
::del *.proto
::del *.data
::del *.log
::del *.txt

::@echo on
python xls_config_tool.py ../%FOLDER_NAME%



::---------------------------------------------------
::第二步：把proto翻译成cs
::---------------------------------------------------
cd ..

set STEP2_PROTO2CS_PATH=.\step2_proto2cs
set PROTO_DESC=protodesc
set SRC_OUT=src

cd %STEP2_PROTO2CS_PATH%

::@echo off
::echo TRY TO DELETE TEMP FILES:
::del *.cs
::del *.protodesc
::del *.txt
if exist %SRC_OUT% rd /s/q %SRC_OUT%
md %SRC_OUT%
if exist %PROTO_DESC% rd /s/q %PROTO_DESC%
md %PROTO_DESC%
@echo on
dir ..\%STEP1_XLS2PROTO_PATH%\output\proto\*.proto /b  > protolist.txt

@echo on
for /f "delims=." %%i in (protolist.txt) do ..\%STEP1_XLS2PROTO_PATH%\protoc --descriptor_set_out=%PROTO_DESC%/%%i.protodesc --proto_path=..\%STEP1_XLS2PROTO_PATH%\output\proto --include_imports ..\%STEP1_XLS2PROTO_PATH%\output\proto\%%i.proto
for /f "delims=." %%i in (protolist.txt) do ProtoGen\protogen -i:%PROTO_DESC%\%%i.protodesc -o:%SRC_OUT%\%%i.cs

cd ..

::---------------------------------------------------
::第三步：将data和cs拷到Assets里
::---------------------------------------------------
@echo off
set OUT_PATH=..\Assets
set DATA_DEST=StreamingAssets\DataConfig
set CS_DEST=Scripts\Killer\DataConfig\ProtoGen


@echo on
copy %STEP1_XLS2PROTO_PATH%\output\bytes\*.bytes %OUT_PATH%\%DATA_DEST%
copy %STEP2_PROTO2CS_PATH%\%SRC_OUT%\*.cs %OUT_PATH%\%CS_DEST%

::---------------------------------------------------
::第四步：清除中间文件
::---------------------------------------------------
::@echo off
::echo TRY TO DELETE TEMP FILES:
::cd %STEP1_XLS2PROTO_PATH%
::del *_pb2.py
::del *_pb2.pyc
::del *.proto
::del *.data
::del *.log
::del *.txt
::cd ..
::cd %STEP2_PROTO2CS_PATH%
::del *.cs
::del *.protodesc
::del *.txt
::cd ..

::---------------------------------------------------
::第五步：结束
::---------------------------------------------------
::cd ..

@echo on
PAUSE