@echo off
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install it from https://www.python.org/downloads/
  pause
  exit /b 1
)
start "" http://127.0.0.1:8000
python server.py
pause
