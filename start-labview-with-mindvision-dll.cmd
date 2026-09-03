@echo off
setlocal

set "REPO_ROOT=%~dp0.."
for %%I in ("%REPO_ROOT%") do set "REPO_ROOT=%%~fI"
set "MINDVISION_DLL_DIR=%REPO_ROOT%\third_party\mindvision\bin\win32"

if not exist "%MINDVISION_DLL_DIR%\MVCAMSDK.dll" (
    echo ERROR: MVCAMSDK.dll was not found at:
    echo   %MINDVISION_DLL_DIR%\MVCAMSDK.dll
    exit /b 2
)

if "%~1"=="" (
    set "LABVIEW_EXE=C:\Program Files (x86)\National Instruments\LabVIEW 2015\LabVIEW.exe"
) else (
    set "LABVIEW_EXE=%~1"
)

if not exist "%LABVIEW_EXE%" (
    echo ERROR: LabVIEW executable was not found at:
    echo   %LABVIEW_EXE%
    echo.
    echo Usage:
    echo   %~nx0 "C:\Path\To\LabVIEW.exe"
    exit /b 3
)

set "PATH=%MINDVISION_DLL_DIR%;%PATH%"
echo Starting LabVIEW with this temporary DLL search directory:
echo   %MINDVISION_DLL_DIR%
start "" "%LABVIEW_EXE%"
endlocal
