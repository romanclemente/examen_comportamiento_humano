@echo off
:loop
echo Lanzando el script...
python "C:\Users\roman\Desktop\Herramientas de clase\Generador de Test\main.py"
echo El script se cerró. Reiniciando en 3 segundos...
timeout /t 3 >nul
goto loop
