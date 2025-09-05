#!/usr/bin/env python3
"""
🚀 GHOST KITTY AUDIO CONVERTER - MEGA ENHANCEMENT INSTALLER 🚀
This script will install all the cool new features and dependencies!
"""

import subprocess
import sys
import os
import platform
from pathlib import Path

def print_banner():
    """Print cool installation banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║     👻🎵 GHOST KITTY AUDIO CONVERTER - MEGA INSTALLER 🎵👻      ║
    ║                                                                  ║
    ║               Installing Enhanced Features & Dependencies         ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Python 3.7+ required")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} - Compatible!")
    return True

def install_package(package_name, display_name=None):
    """Install a Python package"""
    if not display_name:
        display_name = package_name
        
    print(f"\n🔧 Installing {display_name}...")
    
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
        print(f"✅ {display_name} installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {display_name}")
        return False

def check_ffmpeg():
    """Check if FFmpeg is available"""
    print("\n🎵 Checking for FFmpeg...")
    
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ FFmpeg is already installed!")
            return True
    except FileNotFoundError:
        pass
    
    print("⚠️  FFmpeg not found - required for audio conversion")
    
    system = platform.system().lower()
    if system == 'windows':
        print("📦 To install FFmpeg on Windows:")
        print("   1. winget install FFmpeg")
        print("   2. Or download from: https://ffmpeg.org/download.html")
    elif system == 'darwin':  # macOS
        print("📦 To install FFmpeg on macOS:")
        print("   brew install ffmpeg")
    else:  # Linux
        print("📦 To install FFmpeg on Linux:")
        print("   Ubuntu/Debian: sudo apt install ffmpeg")
        print("   CentOS/RHEL: sudo yum install ffmpeg")
        print("   Arch: sudo pacman -S ffmpeg")
    
    return False

def install_enhanced_packages():
    """Install all enhanced feature packages"""
    packages = [
        ('Pillow>=9.0.0', 'Pillow (Enhanced Graphics)'),
        ('numpy>=1.20.0', 'NumPy (Audio Visualization)'),
        ('tkinterdnd2>=0.3.0', 'TkinterDnD2 (Drag & Drop)'),
        ('pygame>=2.1.0', 'Pygame (Audio Processing)'),
        ('matplotlib>=3.5.0', 'Matplotlib (Visualization - Optional)'),
        ('librosa>=0.9.0', 'Librosa (Audio Analysis - Optional)'),
        ('mutagen>=1.45.0', 'Mutagen (Metadata Editing - Optional)')
    ]
    
    print("\n🌈 Installing Enhanced Feature Packages...")
    
    success_count = 0
    optional_failed = []
    
    for package, display_name in packages:
        is_optional = 'Optional' in display_name
        
        if install_package(package, display_name):
            success_count += 1
        elif is_optional:
            optional_failed.append(display_name)
        else:
            print(f"⚠️  Core package {display_name} failed to install")
    
    print(f"\n📊 Installation Summary:")
    print(f"   ✅ Successfully installed: {success_count}/{len(packages)} packages")
    
    if optional_failed:
        print(f"   ⚠️  Optional features not available: {len(optional_failed)}")
        for feature in optional_failed:
            print(f"      - {feature}")
            
    return success_count >= 4  # At least core packages

def create_launch_scripts():
    """Create convenient launch scripts"""
    print("\n🚀 Creating Launch Scripts...")
    
    # Enhanced launcher script
    enhanced_launcher = '''@echo off
echo 👻🎵 Starting Ghost Kitty Audio Converter - MEGA ENHANCED EDITION! 🎵👻
echo.
python main_enhanced.py
pause
'''
    
    # Original launcher (fallback)
    original_launcher = '''@echo off
echo 👻🎵 Starting Ghost Kitty Audio Converter - Original Edition 🎵👻
echo.
python main.py
pause
'''
    
    try:
        # Windows batch files
        with open('launch_enhanced.bat', 'w') as f:
            f.write(enhanced_launcher)
        print("✅ Created launch_enhanced.bat")
        
        with open('launch_original.bat', 'w') as f:
            f.write(original_launcher)
        print("✅ Created launch_original.bat")
        
        # Linux/Mac shell scripts
        enhanced_sh = '''#!/bin/bash
echo "👻🎵 Starting Ghost Kitty Audio Converter - MEGA ENHANCED EDITION! 🎵👻"
echo
python3 main_enhanced.py
'''
        
        original_sh = '''#!/bin/bash
echo "👻🎵 Starting Ghost Kitty Audio Converter - Original Edition 🎵👻"
echo
python3 main.py
'''
        
        with open('launch_enhanced.sh', 'w') as f:
            f.write(enhanced_sh)
        os.chmod('launch_enhanced.sh', 0o755)
        print("✅ Created launch_enhanced.sh")
        
        with open('launch_original.sh', 'w') as f:
            f.write(original_sh)
        os.chmod('launch_original.sh', 0o755)
        print("✅ Created launch_original.sh")
        
    except Exception as e:
        print(f"⚠️  Could not create launch scripts: {e}")

def create_feature_guide():
    """Create a guide for the new features"""
    guide_content = """# 🚀 GHOST KITTY MEGA ENHANCEMENT GUIDE 🚀

## 🎨 New Visual Features

### 🌈 Unlimited Dynamic Themes
- **Random Theme Button**: Click "🎲 RANDOM THEME" for instant new cyberpunk themes
- **Preset Themes**: Click "🎨 PRESET THEMES" to choose from curated collections
- **Auto Theme Generation**: Every startup gets a unique theme automatically

### ✨ Enhanced Visual Effects
- **Particle System**: Animated background particles with multiple effect types
- **Enhanced Progress Bar**: Animated gradient progress with glow effects
- **Hover Effects**: Buttons glow and pulse when you hover over them
- **Theme Transitions**: Smooth animated theme changes

## 🎵 Enhanced Audio Features

### 📂 Drag & Drop Support
- Drag audio files directly onto the window
- Drag entire folders for batch processing
- Visual feedback for dropped files

### 🎛️ Enhanced Quality Settings
- More format support: MP3, WAV, FLAC, OGG, AAC, M4A
- Quality presets: Low, Medium, High, Highest
- Advanced codec settings for professional results

### 📊 Better File Management
- Enhanced file list with size information
- Real-time status updates during conversion
- Better error handling and reporting

## 🎮 New Themes Available

### Predefined Epic Themes:
- **Ghost Kitty Classic**: The original neon green and pink
- **Vaporwave Dreams**: Pink and cyan retro vibes
- **Synthwave Sunset**: Orange and yellow energy
- **Matrix Green**: Classic digital rain aesthetic
- **Neon Tokyo**: Red and blue cyberpunk city
- **Electric Teal**: Cool cyan and teal tones
- **Cyber Orange**: Warm orange cyber aesthetic

### Generated Themes:
- **Infinite Variations**: HSV color generation creates unlimited themes
- **Epic Names**: "Ultra Plasma Boost", "Mega Neural Prime", etc.
- **Harmonic Colors**: Mathematically perfect color combinations

## 🚀 How to Use Enhanced Features

### Quick Start:
1. Run `launch_enhanced.bat` (Windows) or `./launch_enhanced.sh` (Linux/Mac)
2. Try different themes with the theme buttons
3. Drag and drop audio files for instant addition
4. Watch the enhanced progress animations

### Pro Tips:
- Use "🎲 RANDOM THEME" to discover new color combinations
- The particle effects adapt to your current theme
- Enhanced progress bar shows smooth animations during conversion
- All themes maintain the cyberpunk aesthetic while offering variety

## 🛠️ Troubleshooting

If enhanced features don't work:
1. Run `python mega_installer.py` again
2. Check that all dependencies installed successfully
3. Use the original version as fallback: `python main.py`

## 🎵 Enjoy Your Enhanced Ghost Kitty Experience! 🎵

The enhanced version maintains all original functionality while adding:
- Better visual feedback
- More customization options  
- Enhanced user experience
- Professional-grade features

Have fun exploring all the new themes and features! 👻✨
"""
    
    try:
        with open('ENHANCEMENT_GUIDE.md', 'w', encoding='utf-8') as f:
            f.write(guide_content)
        print("✅ Created ENHANCEMENT_GUIDE.md")
    except Exception as e:
        print(f"⚠️  Could not create feature guide: {e}")

def main():
    """Main installation process"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        input("Press Enter to exit...")
        return
    
    # Check FFmpeg
    ffmpeg_available = check_ffmpeg()
    
    # Install enhanced packages
    packages_ok = install_enhanced_packages()
    
    # Create launch scripts
    create_launch_scripts()
    
    # Create feature guide
    create_feature_guide()
    
    # Final summary
    print("\n" + "="*70)
    print("🎉 GHOST KITTY MEGA ENHANCEMENT INSTALLATION COMPLETE! 🎉")
    print("="*70)
    
    if packages_ok:
        print("✅ Enhanced features ready to use!")
        print("\n🚀 To start the ENHANCED version:")
        print("   Windows: launch_enhanced.bat")
        print("   Linux/Mac: ./launch_enhanced.sh")
        print("   Manual: python main_enhanced.py")
    else:
        print("⚠️  Some enhanced features may not work properly")
        print("   You can still use the original version: python main.py")
    
    if not ffmpeg_available:
        print("\n⚠️  Don't forget to install FFmpeg for audio conversion!")
    
    print("\n📖 Read ENHANCEMENT_GUIDE.md for all the new features!")
    print("👻🎵 Enjoy your enhanced Ghost Kitty experience! 🎵👻")
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
