@echo off
echo 👻🎵 GHOST KITTY AUDIO CONVERTER - RELEASE PREP 🎵👻
echo =================================================

:: Create release directory
if not exist release mkdir release

:: Copy essential files for release
echo 📦 Copying release files...
copy main.py release\
copy launch.bat release\
copy README.md release\
copy LICENSE release\
copy requirements.txt release\
copy CHANGELOG.md release\
copy CONTRIBUTING.md release\

:: Create release info
echo 👻🎵 GHOST KITTY AUDIO CONVERTER v1.0.0 🎵👻 > release\RELEASE_INFO.txt
echo. >> release\RELEASE_INFO.txt
echo Release Date: %date% >> release\RELEASE_INFO.txt
echo Platform: Windows (Primary), Cross-platform compatible >> release\RELEASE_INFO.txt
echo. >> release\RELEASE_INFO.txt
echo 📁 Release Contents: >> release\RELEASE_INFO.txt
echo - main.py           # Complete self-contained application >> release\RELEASE_INFO.txt
echo - launch.bat        # Windows launcher script >> release\RELEASE_INFO.txt
echo - README.md         # Full documentation >> release\RELEASE_INFO.txt
echo - LICENSE           # MIT License >> release\RELEASE_INFO.txt
echo - requirements.txt  # Setup instructions >> release\RELEASE_INFO.txt
echo - CHANGELOG.md      # Version history >> release\RELEASE_INFO.txt
echo - CONTRIBUTING.md   # Contribution guidelines >> release\RELEASE_INFO.txt
echo. >> release\RELEASE_INFO.txt
echo 🚀 Quick Start: >> release\RELEASE_INFO.txt
echo 1. Install FFmpeg: winget install FFmpeg >> release\RELEASE_INFO.txt
echo 2. Run: python main.py >> release\RELEASE_INFO.txt
echo 3. Enjoy unlimited dynamic themes! >> release\RELEASE_INFO.txt
echo. >> release\RELEASE_INFO.txt
echo ✨ Features: >> release\RELEASE_INFO.txt
echo - 🎨 Unlimited dynamic themes with cyberpunk aesthetics >> release\RELEASE_INFO.txt
echo - 🎵 Universal audio conversion (MP3, WAV, FLAC, OGG, AAC, M4A, WMA, MP4, AVI) >> release\RELEASE_INFO.txt
echo - ⚡ Batch processing with unlimited file support >> release\RELEASE_INFO.txt
echo - 🖥️ Electronic GUI with neon styling >> release\RELEASE_INFO.txt
echo - 🚀 Self-contained single-file application >> release\RELEASE_INFO.txt
echo. >> release\RELEASE_INFO.txt
echo Made with 💜 for the audio conversion community >> release\RELEASE_INFO.txt

echo ✅ Release files prepared in .\release\ directory
echo.
echo 🎯 Ready for GitHub release!
echo Files prepared:
dir release

echo.
echo 📋 Next steps:
echo 1. Create GitHub repository
echo 2. Upload release files
echo 3. Create release tag (v1.0.0)
echo 4. Share with the world! 🌍

pause
