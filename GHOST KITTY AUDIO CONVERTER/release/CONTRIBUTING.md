# 🤝 Contributing to Ghost Kitty Audio Converter

Thank you for your interest in contributing to the **Ghost Kitty Audio Converter**! 👻🎵

We welcome contributions from the community and are pleased you want to help make this project even more awesome!

## 🌟 Ways to Contribute

### 🐛 **Bug Reports**
- Report bugs via [GitHub Issues](https://github.com/yourusername/ghost-kitty-audio-converter/issues)
- Include detailed steps to reproduce
- Mention your OS and Python version
- Attach log files if available (`ghostkitty_converter.log`)

### 💡 **Feature Requests**
- Suggest new features via [GitHub Issues](https://github.com/yourusername/ghost-kitty-audio-converter/issues)
- Explain the use case and benefits
- Consider cyberpunk/electronic aesthetic alignment
- Propose implementation ideas if you have them

### 🎨 **Theme Contributions**
- Create new predefined themes
- Suggest theme name combinations
- Share color scheme ideas
- Propose new theme categories

### 💻 **Code Contributions**
- Fix bugs and issues
- Implement new features
- Improve performance
- Enhance documentation
- Add tests and error handling

## 🚀 Getting Started

### 1. **Setup Development Environment**

```bash
# Clone the repository
git clone https://github.com/yourusername/ghost-kitty-audio-converter.git
cd ghost-kitty-audio-converter

# Install FFmpeg
winget install FFmpeg

# Test the application
python main.py
```

### 2. **Development Guidelines**

#### **Code Style**
- Follow Python PEP 8 guidelines
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Keep the electronic/cyberpunk theme consistent

#### **File Structure**
- All functionality should remain in `main.py` (single-file design)
- Keep the self-contained architecture
- No additional Python dependencies beyond standard library

#### **Theme Development**
- Use HSV color space for theme generation
- Maintain cyberpunk/electronic aesthetic
- Ensure good contrast and readability
- Test themes with different content

### 3. **Coding Standards**

```python
# Example function with proper documentation
def generate_theme_variation(self, base_hue: float) -> dict:
    """
    Generate a theme variation based on a base hue.
    
    Args:
        base_hue (float): Base hue value (0-360)
        
    Returns:
        dict: Complete theme dictionary with all color properties
    """
    # Implementation here
    pass
```

## 🔄 Contribution Process

### 1. **Fork & Clone**
```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/yourusername/ghost-kitty-audio-converter.git
```

### 2. **Create Feature Branch**
```bash
# Create and switch to a new branch
git checkout -b feature/amazing-new-feature
```

### 3. **Make Changes**
- Implement your changes
- Test thoroughly
- Maintain single-file architecture
- Follow coding standards

### 4. **Test Your Changes**
```bash
# Test the application
python main.py

# Test theme system
python -c "from main import ThemeManager; tm = ThemeManager(); print(tm.get_random_theme())"

# Test audio converter (requires FFmpeg)
python -c "from main import AudioConverter; ac = AudioConverter(); print('FFmpeg:', ac.ffmpeg_path)"
```

### 5. **Commit & Push**
```bash
# Commit your changes
git add .
git commit -m "✨ Add amazing new feature

- Describe what the feature does
- Mention any breaking changes
- Reference related issues"

# Push to your fork
git push origin feature/amazing-new-feature
```

### 6. **Create Pull Request**
- Open a PR against the main repository
- Describe your changes clearly
- Include screenshots if UI changes
- Reference related issues

## 🎨 Theme Development Guide

### **Creating New Predefined Themes**

```python
{
    'name': 'Your Theme Name',
    'bg_dark': '#0a0a0a',      # Dark background
    'bg_medium': '#1a1a1a',    # Medium background  
    'bg_light': '#2a2a2a',     # Light background
    'primary': '#ff0080',      # Primary accent color
    'secondary': '#0080ff',    # Secondary accent color
    'accent': '#80ff00',       # Tertiary accent color
    'bright': '#ff40a0',       # Bright variant
    'dark': '#cc0060',         # Dark variant
    'text_primary': '#ff0080', # Primary text color
    'text_secondary': '#0080ff', # Secondary text color
    'text_accent': '#80ff00',  # Accent text color
    'button_colors': [         # Button color variations
        '#ff0080', '#0080ff', '#80ff00', 
        '#ff40a0', '#cc0060', '#40ff80'
    ]
}
```

### **Theme Naming Convention**
- Use cyberpunk/electronic terminology
- Format: `"[Prefix] [Suffix]"`
- Prefixes: Neon, Cyber, Ghost, Digital, Matrix, Quantum, Electric, etc.
- Suffixes: Wave, Pulse, Storm, Flow, Rush, Blast, Flash, etc.

## 🐛 Bug Reports

### **Good Bug Report Example**
```
**Bug Description:** Theme colors not applying to progress bar

**Steps to Reproduce:**
1. Start application
2. Load files for conversion
3. Change theme using "NEW THEME" button
4. Progress bar still shows old colors

**Expected Behavior:** Progress bar should update to new theme colors

**Environment:**
- OS: Windows 11
- Python: 3.11.2
- FFmpeg: 7.1.1

**Log Output:**
[Attach relevant log entries from ghostkitty_converter.log]
```

## 💡 Feature Request Template

```
**Feature Name:** [Feature name]

**Description:** [Clear description of the feature]

**Use Case:** [Why this feature would be useful]

**Implementation Ideas:** [Optional: How it could be implemented]

**Theme Compatibility:** [How it fits with the electronic aesthetic]
```

## 📋 Code Review Checklist

Before submitting a PR, ensure:

- [ ] ✅ Code follows Python PEP 8 guidelines
- [ ] ✅ All functions have proper docstrings
- [ ] ✅ Single-file architecture maintained
- [ ] ✅ No new external dependencies added
- [ ] ✅ Cyberpunk theme consistency maintained
- [ ] ✅ Error handling implemented
- [ ] ✅ Application tested and working
- [ ] ✅ Changes documented in comments

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Special thanks in documentation

## 📞 Getting Help

- **Questions:** Open a [GitHub Discussion](https://github.com/yourusername/ghost-kitty-audio-converter/discussions)
- **Issues:** Use [GitHub Issues](https://github.com/yourusername/ghost-kitty-audio-converter/issues)
- **Documentation:** Check the README.md and code comments

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

<div align="center">

**Thank you for contributing to Ghost Kitty Audio Converter!** 🙏

*Together we're building the coolest audio converter in the cyberpunk universe* 🌈

</div>
