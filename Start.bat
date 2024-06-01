echo off
cls
title Baconbuddy ^| Updating python
echo [-] Updating python
python.exe -m pip install --upgrade pip >nul
cls
echo [+] Updated python
title Baconbuddy ^| Installing packages
echo [-] Installing tkinter
pip install tk >nul
cls
echo [+] Updated python
echo [+] Installed tkinter
echo [-] Installing Pillow
pip install pillow >nul
cls
echo [+] Updated python
echo [+] Installed tkinter
echo [+] Installed Pillow
echo [-] Installing pygame
pip install pygame >nul
cls
echo [+] Updated python
echo [+] Installed tkinter
echo [+] Installed Pillow
echo [+] Installed pygame
echo [-] Installing winshell
pip install winshell >nul
cls
echo [+] Updated python
echo [+] Installed tkinter
echo [+] Installed Pillow
echo [+] Installed pygame
echo [+] Installed winshell
echo [+] Installed all packages
echo [CONSOLE] Close this.
pythonw bacon.pyw
pause
exit