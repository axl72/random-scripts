@echo off
cd /d "%~dp0"

:: Ejecuta el script de Python
python consignacion_intek.py %*

:: Mantiene la consola abierta si ocurre un error
if %errorlevel% neq 0 pause