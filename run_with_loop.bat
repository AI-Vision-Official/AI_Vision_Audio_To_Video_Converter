@echo off
cd /d "%~dp0"
echo ===============================
echo 🔁 Audio naar Video met Loop Video
echo ===============================

:: Check of Python aanwezig is
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is niet geïnstalleerd.
    echo 👉 Download: https://www.python.org/downloads/
    pause
    exit /b
)

:: Benodigde packages installeren
echo 📦 Installeren van moviepy...
pip install moviepy imageio[ffmpeg]

:: Script uitvoeren
echo ▶️ Start audio_to_video_with_loop.py...
python audio_to_video_with_loop.py

echo ✅ Afgerond!
pause
