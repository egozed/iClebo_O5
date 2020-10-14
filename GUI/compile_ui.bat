@echo off
set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PQTNAME=%UIDIR%pyqt\%FILENAME%_ui.py
set PSDNAME=%UIDIR%pyside\%FILENAME%_ui.py
mkdir %UIDIR%pyqt
mkdir %UIDIR%pyside
echo Compile %UIFILE%(xml)
echo to     %PQTNAME%(python)
CALL pyuic5 %UIFILE% -o %PQTNAME%
echo Compile %UIFILE%(xml)
echo to     %PSDNAME%(python)
CALL pyside2-uic %UIFILE% -o %PSDNAME%
