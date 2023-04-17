@echo off
cd %~dp0
call playenv\scripts\activate.bat
python playsound.py
pause
