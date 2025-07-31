#!/bin/bash
# 🚀 Ghost Kitty Audio Converter - Release Preparation Script

echo "👻🎵 GHOST KITTY AUDIO CONVERTER - RELEASE PREP 🎵👻"
echo "================================================="

# Create release directory
mkdir -p release

# Copy essential files for release
echo "📦 Copying release files..."
cp main.py release/
cp launch.bat release/
cp README.md release/
cp LICENSE release/
cp requirements.txt release/
cp CHANGELOG.md release/
cp CONTRIBUTING.md release/

# Create a release package info
cat > release/RELEASE_INFO.txt << EOF
👻🎵 GHOST KITTY AUDIO CONVERTER v1.0.0 🎵👻

Release Date: $(date)
Platform: Windows (Primary), Cross-platform compatible

📁 Release Contents:
- main.py           # Complete self-contained application
- launch.bat        # Windows launcher script  
- README.md         # Full documentation
- LICENSE           # MIT License
- requirements.txt  # Setup instructions
- CHANGELOG.md      # Version history
- CONTRIBUTING.md   # Contribution guidelines

🚀 Quick Start:
1. Install FFmpeg: winget install FFmpeg
2. Run: python main.py
3. Enjoy unlimited dynamic themes!

✨ Features:
- 🎨 Unlimited dynamic themes with cyberpunk aesthetics
- 🎵 Universal audio conversion (MP3, WAV, FLAC, OGG, AAC, M4A, WMA, MP4, AVI)
- ⚡ Batch processing with unlimited file support
- 🖥️ Electronic GUI with neon styling
- 🚀 Self-contained single-file application

Made with 💜 for the audio conversion community
EOF

echo "✅ Release files prepared in ./release/ directory"
echo ""
echo "🎯 Ready for GitHub release!"
echo "Files to upload:"
ls -la release/

echo ""
echo "📋 Next steps:"
echo "1. Create GitHub repository"
echo "2. Upload release files"
echo "3. Create release tag (v1.0.0)"
echo "4. Share with the world! 🌍"
