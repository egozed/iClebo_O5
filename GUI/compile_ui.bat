set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PQTNAME=%UIDIR%pyqt\%FILENAME%_ui.py
set PSDNAME=%UIDIR%pyside\%FILENAME%_ui.py
mkdir %UIDIR%pyqt
mkdir %UIDIR%pyside
echo compile for x86
CALL "C:\Program Files\Python38-32\Scripts\pyuic5.exe" %UIFILE% -o %PQTNAME%
CALL "C:\Program Files\Python38-32\Scripts\pyside2-uic.exe" %UIFILE% -o %PSDNAME%
echo compile for x64
CALL "C:\Program Files\Python38\Scripts\pyuic5.exe" %UIFILE% -o %PQTNAME%
CALL "C:\Program Files\Python38\Scripts\pyside2-uic.exe" %UIFILE% -o %PSDNAME%
