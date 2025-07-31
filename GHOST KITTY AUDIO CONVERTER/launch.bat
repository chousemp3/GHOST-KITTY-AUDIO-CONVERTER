@echo off
title Ghost Kitty Audio Converter
color 0A

echo.
echo    ╔═══════════════════════════════════════════════════════════╗
echo    ║                                                           ║
echo    ║        👻🎵 GHOST KITTY AUDIO CONVERTER 🎵👻             ║
echo    ║                                                           ║
echo    ║           SUPER COOL ELECTRONIC STYLE CONVERTER          ║
echo    ║                                                           ║
echo    ╚═══════════════════════════════════════════════════════════╝
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH!
    echo Please install Python 3.7+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python is installed
python --version

:: Check if main.py exists
if not exist "main.py" (
    echo ❌ main.py not found in current directory!
    echo Please make sure you're running this from the Ghost Kitty folder
    pause
    exit /b 1
)

echo ✅ Ghost Kitty files found
echo.
echo 🚀 Launching Ghost Kitty Audio Converter...
echo.

:: Launch the application
python main.py

echo.
echo Thanks for using Ghost Kitty Audio Converter! 👻🎵
pause
