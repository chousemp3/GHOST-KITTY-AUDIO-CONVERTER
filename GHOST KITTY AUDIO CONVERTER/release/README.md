# 👻🎵 GHOST KITTY AUDIO CONVERTER 🎵👻

> **Super Cool Electronic Style Audio Converter with Unlimited Dynamic Themes**

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

A **cyberpunk-styled** audio converter that can convert any audio file to any format with **unlimited batch processing** and **unlimited dynamic themes** that change with every startup!

## ✨ Features

### 🎨 **Unlimited Dynamic Themes**
- **Infinite Theme Variations**: HSV color generation creates unlimited unique themes
- **Startup Randomization**: Different cyberpunk theme every time you launch
- **50+ Predefined Themes**: "Neon Dream", "Cyber Pulse", "Matrix Code", "Hologram Drive", etc.
- **Live Theme Switching**: Change themes on-the-fly with the click of a button
- **Electronic Aesthetic**: All themes maintain cyberpunk/electronic styling

### � **Universal Audio Conversion**
- **All Major Formats**: MP3, WAV, FLAC, OGG, AAC, M4A, WMA, MP4, AVI
- **Quality Settings**: Low, Medium, High, Highest quality options
- **Batch Processing**: Convert unlimited files simultaneously
- **Folder Processing**: Add entire folders of audio files at once
- **Progress Tracking**: Real-time conversion progress with file-by-file status

### 🖥️ **Electronic GUI Experience**
- **Cyberpunk Interface**: Neon colors, electronic styling, futuristic design
- **Dynamic Color Schemes**: Every element adapts to the current theme
- **Responsive Design**: Resizable interface that scales beautifully
- **Electronic Progress Bars**: Custom neon-styled progress indicators
- **Themed File Browser**: Color-coordinated file selection and management

### ⚡ **Performance & Reliability**
- **FFmpeg Integration**: Professional-grade audio conversion engine
- **Multi-threading**: Non-blocking UI during conversion
- **Error Handling**: Comprehensive error reporting and recovery
- **Logging**: Detailed conversion logs for debugging
- **Memory Efficient**: Optimized for large batch operations  

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+** 
- **FFmpeg** (Required for audio conversion)

### Installation

1. **Clone or Download** the Ghost Kitty Converter:
```bash
git clone https://github.com/your-username/ghost-kitty-audio-converter.git
cd ghost-kitty-audio-converter
```

2. **Install FFmpeg**:

**Windows:**
```bash
# Download from https://ffmpeg.org/download.html
# Extract to C:\ffmpeg\
# Add C:\ffmpeg\bin to your PATH
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# CentOS/RHEL
sudo yum install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

**macOS:**
```bash
# Homebrew
brew install ffmpeg

# MacPorts
sudo port install ffmpeg
```

3. **Run the Ghost Kitty!**:

**Windows:**
```bash
# Double-click launch.bat
# OR
python main.py
```

**Linux/macOS:**
```bash
python3 main.py
```

## 🎛️ How to Use

### 🎵 Adding Files
- **Single Files**: Click `🎵 ADD FILES` to select individual audio files
- **Batch Folders**: Click `📁 ADD FOLDER` to add entire directories
- **Supported Formats**: MP3, WAV, FLAC, OGG, AAC, M4A, WMA, MP4, AVI, and more!

### ⚙️ Configuration
- **Output Format**: Choose your target format (MP3, WAV, FLAC, etc.)
- **Quality Settings**:
  - 🔴 **Low**: Fastest conversion, smaller files
  - 🟡 **Medium**: Balanced quality and size
  - 🟢 **High**: Excellent quality (recommended)
  - 🔥 **Highest**: Maximum quality, larger files

### 🚀 Conversion
1. Add your audio files
2. Select output format and quality
3. Choose output directory
4. Hit `🚀 START CONVERSION`
5. Watch the electronic progress bars! ⚡

### 📊 Monitoring
- **Real-time Progress**: See conversion progress with animated bars
- **File Status**: Track each file's conversion state
- **Live Stats**: Monitor total files, current file, and completion rate

## 🛠️ Development

### Project Structure
```
ghost-kitty-audio-converter/
├── main.py                 # Main application (self-contained)
├── launch.bat             # Windows launcher script
├── requirements.txt       # Dependencies
├── README.md             # This awesome readme
└── ghostkitty_converter.log  # Conversion logs (created at runtime)
```

### Code Features
- **Self-Contained**: All functionality in a single main.py file
- **Error Handling**: Comprehensive error catching and logging
- **Threading**: Non-blocking UI during conversions
- **Logging**: Detailed conversion logs for debugging
- **Electronic Theme**: Built-in cyberpunk styling

## 🔧 FFmpeg Installation Guide

### Windows
1. Download FFmpeg from: https://ffmpeg.org/download.html
2. Choose 'Windows builds' → 'Windows builds by BtbN'
3. Download the latest release (ffmpeg-master-latest-win64-gpl.zip)
4. Extract to C:\\ffmpeg\\
5. Add C:\\ffmpeg\\bin to your PATH environment variable:
   - Open System Properties → Advanced → Environment Variables
   - Edit 'Path' in System Variables
   - Add new entry: C:\\ffmpeg\\bin
   - Click OK and restart Ghost Kitty

Alternative (Package Managers):
- Chocolatey: `choco install ffmpeg`
- Scoop: `scoop install ffmpeg`
- Winget: `winget install FFmpeg`

### Linux
- Ubuntu/Debian: `sudo apt update && sudo apt install ffmpeg`
- CentOS/RHEL: `sudo yum install epel-release && sudo yum install ffmpeg`
- Fedora: `sudo dnf install ffmpeg`
- Arch Linux: `sudo pacman -S ffmpeg`
- openSUSE: `sudo zypper install ffmpeg`

### macOS
- Homebrew: `brew install ffmpeg`
- MacPorts: `sudo port install ffmpeg`
- Download binary: https://evermeet.cx/ffmpeg/

## 🎵 Supported Formats

### Input Formats
- **Audio**: MP3, WAV, FLAC, OGG, AAC, M4A, WMA
- **Video**: MP4, AVI, MKV, MOV, WMV, 3GP, WebM

### Output Formats
- **Audio**: MP3, WAV, FLAC, OGG, AAC, M4A, WMA
- **Video**: MP4, AVI

## 🐛 Troubleshooting

### Common Issues
- **FFmpeg Not Found**: Install FFmpeg and add it to your PATH
- **No files appearing**: Check file extensions are supported
- **Conversion failed**: Verify FFmpeg installation and file permissions
- **Slow conversion**: Try lower quality settings or check system resources
- **GUI not responding**: Ensure Python/Tkinter is properly installed

## 👻 About Ghost Kitty

Ghost Kitty is all about making audio conversion **fun**, **fast**, and **fantastic**! 

- 🎵 **Music Lover Friendly**: Perfect for DJs, producers, and music enthusiasts
- 🎮 **Gamer Approved**: Convert game audio and music collections
- 💼 **Professional Grade**: Suitable for studios and content creators
- 🔥 **Community Driven**: Built with love for the audio community

---

**Made with 💜 by the Ghost Kitty Team**

*Transform your audio, unleash your creativity! 👻🎵*

![Ghost Kitty Footer](https://img.shields.io/badge/POWERED%20BY-GHOST%20KITTY-00ff41?style=for-the-badge&logo=ghost&logoColor=white)
