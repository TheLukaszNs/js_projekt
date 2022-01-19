@echo off
title Projekt - Zadanie Lizak
:menu
cls
echo ============================================================
echo        ============  MENU PROJEKTU  ===============
echo ============================================================
echo 1. Generuj raport
echo 2. Generuj raport (na podstawie gotowych danych)
echo 3. Wyswietl ostatni raport
echo 4. Usuwanie raportow
echo 5. Generuj dane
echo 6. Wyjscie
echo.
set /p option=Wybierz opcje: 
if %option%==1 goto :generuj
if %option%==2 goto :generujhtml
if %option%==3 goto :wyswietl
if %option%==4 goto :usun
if %option%==5 goto :dane
if %option%==6 goto :eof
goto :menu

:generuj
del .\out\*.txt
call ./venv/scripts/activate.bat
call python py1.py

:generujhtml:
call python py2.py
echo Zakonczono generowanie raportu!
pause
goto :menu

:wyswietl
for /f "eol=: delims=" %%F in ('dir /b /od .\raporty\*.html') do @set "newest=%%F"
call ".\raporty\%newest%"
pause
goto :menu

:dane
del .\in\*.txt
set /p numfiles=Ile plikow wejsciowych do generacji?:
call python generator.py %numfiles%
pause
goto :menu

:usun
del .\raporty\*.html
pause
goto :menu

:eof
pause