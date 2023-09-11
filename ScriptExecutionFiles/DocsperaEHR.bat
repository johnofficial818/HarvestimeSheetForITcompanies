@REM cd ..
@REM echo %cd%
@REM set currentdate=%DATE:~3,3%%DATE:~0,3%%DATE:~6,4%
@REM echo %currentdate%
@REM set environ=dev
@REM echo %environ%
python -m pytest ../testsuites/test_harvest.py
