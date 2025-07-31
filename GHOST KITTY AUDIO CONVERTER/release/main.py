#!/usr/bin/env python3
"""
🎵 GHOST KITTY AUDIO CONVERTER 🎵
Super Cool Electronic Style Audio Converter
Converts any audio file to any format with unlimited batch processing!
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import threading
import subprocess
import shutil
import platform
from pathlib import Path
import logging
from typing import Optional
import random
import colorsys

# Theme Manager Class for Unlimited Dynamic Themes
class ThemeManager:
    """Dynamic theme manager with unlimited color schemes"""
    
    def __init__(self):
        self.current_theme = self.generate_random_theme()
        
    def generate_random_theme(self):
        """Generate a completely random theme with cyberpunk aesthetics"""
        # Generate base hue (0-360)
        base_hue = random.uniform(0, 360)
        
        # Generate complementary colors
        primary_hue = base_hue
        secondary_hue = (base_hue + 120) % 360
        accent_hue = (base_hue + 240) % 360
        
        # Convert to RGB with high saturation and varying brightness
        primary_color = self.hsv_to_hex(primary_hue, 0.9, 0.8)
        secondary_color = self.hsv_to_hex(secondary_hue, 0.8, 0.7)
        accent_color = self.hsv_to_hex(accent_hue, 0.85, 0.75)
        
        # Generate additional colors
        bright_primary = self.hsv_to_hex(primary_hue, 0.7, 1.0)
        dark_primary = self.hsv_to_hex(primary_hue, 0.9, 0.4)
        
        theme = {
            'name': self.generate_theme_name(),
            'bg_dark': '#0a0a0a',
            'bg_medium': '#1a1a1a',
            'bg_light': '#2a2a2a',
            'primary': primary_color,
            'secondary': secondary_color,
            'accent': accent_color,
            'bright': bright_primary,
            'dark': dark_primary,
            'text_primary': primary_color,
            'text_secondary': secondary_color,
            'text_accent': accent_color,
            'button_colors': [
                primary_color, secondary_color, accent_color,
                bright_primary, self.hsv_to_hex((primary_hue + 60) % 360, 0.8, 0.8),
                self.hsv_to_hex((primary_hue + 180) % 360, 0.9, 0.7)
            ]
        }
        
        return theme
        
    def hsv_to_hex(self, h, s, v):
        """Convert HSV to hex color"""
        rgb = colorsys.hsv_to_rgb(h / 360, s, v)
        return f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"
        
    def generate_theme_name(self):
        """Generate a cool cyberpunk theme name"""
        prefixes = [
            "Neon", "Cyber", "Ghost", "Digital", "Matrix", "Quantum", "Electric",
            "Plasma", "Laser", "Hologram", "Binary", "Neural", "Synthetic", "Chrome",
            "Vapor", "Retro", "Glitch", "Pixel", "Data", "Vector"
        ]
        
        suffixes = [
            "Wave", "Pulse", "Storm", "Flow", "Rush", "Blast", "Flash", "Surge",
            "Glow", "Beam", "Stream", "Force", "Energy", "Power", "Vibe", "Zone",
            "Core", "Grid", "Net", "Link", "Drive", "Code", "Sync", "Loop"
        ]
        
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"
        
    def get_predefined_themes(self):
        """Get some predefined awesome themes"""
        themes = [
            {
                'name': 'Classic Ghost Kitty',
                'bg_dark': '#0a0a0a',
                'bg_medium': '#1a1a1a',
                'bg_light': '#2a2a2a',
                'primary': '#00ff41',
                'secondary': '#ff0080',
                'accent': '#0080ff',
                'bright': '#40ff80',
                'dark': '#00cc33',
                'text_primary': '#00ff41',
                'text_secondary': '#ff0080',
                'text_accent': '#0080ff',
                'button_colors': ['#ff0080', '#0080ff', '#ff4000', '#00ff00', '#8000ff', '#ffff00']
            },
            {
                'name': 'Cyberpunk Red',
                'bg_dark': '#0a0a0a',
                'bg_medium': '#1a0505',
                'bg_light': '#2a0a0a',
                'primary': '#ff0040',
                'secondary': '#ff4080',
                'accent': '#ff8000',
                'bright': '#ff6080',
                'dark': '#cc0030',
                'text_primary': '#ff0040',
                'text_secondary': '#ff4080',
                'text_accent': '#ff8000',
                'button_colors': ['#ff0040', '#ff4080', '#ff8000', '#ff6080', '#cc0030', '#ff0080']
            },
            {
                'name': 'Electric Blue',
                'bg_dark': '#0a0a0a',
                'bg_medium': '#050a1a',
                'bg_light': '#0a0a2a',
                'primary': '#0080ff',
                'secondary': '#40a0ff',
                'accent': '#80c0ff',
                'bright': '#60b0ff',
                'dark': '#0060cc',
                'text_primary': '#0080ff',
                'text_secondary': '#40a0ff',
                'text_accent': '#80c0ff',
                'button_colors': ['#0080ff', '#40a0ff', '#80c0ff', '#60b0ff', '#0060cc', '#00c0ff']
            },
            {
                'name': 'Toxic Green',
                'bg_dark': '#0a0a0a',
                'bg_medium': '#0a1a0a',
                'bg_light': '#0a2a0a',
                'primary': '#00ff00',
                'secondary': '#80ff00',
                'accent': '#40ff40',
                'bright': '#60ff60',
                'dark': '#00cc00',
                'text_primary': '#00ff00',
                'text_secondary': '#80ff00',
                'text_accent': '#40ff40',
                'button_colors': ['#00ff00', '#80ff00', '#40ff40', '#60ff60', '#00cc00', '#20ff20']
            },
            {
                'name': 'Purple Haze',
                'bg_dark': '#0a0a0a',
                'bg_medium': '#1a051a',
                'bg_light': '#2a0a2a',
                'primary': '#8000ff',
                'secondary': '#a040ff',
                'accent': '#c080ff',
                'bright': '#b060ff',
                'dark': '#6000cc',
                'text_primary': '#8000ff',
                'text_secondary': '#a040ff',
                'text_accent': '#c080ff',
                'button_colors': ['#8000ff', '#a040ff', '#c080ff', '#b060ff', '#6000cc', '#ff00ff']
            }
        ]
        
        return themes
        
    def get_random_theme(self):
        """Get a random theme (predefined or generated)"""
        if random.random() < 0.3:  # 30% chance for predefined themes
            themes = self.get_predefined_themes()
            return random.choice(themes)
        else:  # 70% chance for generated themes
            return self.generate_random_theme()
            
    def apply_theme_variation(self, base_theme):
        """Apply random variations to a theme"""
        # Randomly adjust brightness and saturation
        variation = random.uniform(-0.1, 0.1)
        
        # Create variations of the base theme
        varied_theme = base_theme.copy()
        
        # Add some random sparkle colors
        sparkle_hues = [random.uniform(0, 360) for _ in range(3)]
        sparkle_colors = [self.hsv_to_hex(h, 0.8, 0.9) for h in sparkle_hues]
        
        varied_theme['button_colors'].extend(sparkle_colors)
        
        return varied_theme
class AudioConverter:
    """Core audio conversion engine using FFmpeg"""
    
    def __init__(self):
        self.setup_logging()
        self.ffmpeg_path = self.find_ffmpeg()
        
        # Quality settings for different formats
        self.quality_settings = {
            'mp3': {
                'low': ['-b:a', '128k'],
                'medium': ['-b:a', '192k'],
                'high': ['-b:a', '320k'],
                'highest': ['-b:a', '320k', '-q:a', '0']
            },
            'wav': {
                'low': ['-ar', '22050'],
                'medium': ['-ar', '44100'],
                'high': ['-ar', '48000'],
                'highest': ['-ar', '96000']
            },
            'flac': {
                'low': ['-compression_level', '0'],
                'medium': ['-compression_level', '5'],
                'high': ['-compression_level', '8'],
                'highest': ['-compression_level', '12']
            },
            'ogg': {
                'low': ['-b:a', '96k'],
                'medium': ['-b:a', '160k'], 
                'high': ['-b:a', '256k'],
                'highest': ['-b:a', '500k']
            }
        }
        
    def setup_logging(self):
        """Setup logging for conversion tracking"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('ghostkitty_converter.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def find_ffmpeg(self) -> Optional[str]:
        """Find FFmpeg executable"""
        # Add more possible paths including winget installation location
        import os
        user_profile = os.environ.get('USERPROFILE', '')
        local_app_data = os.environ.get('LOCALAPPDATA', '')
        
        possible_paths = [
            'ffmpeg',
            'ffmpeg.exe',
            r'C:\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe',
            os.path.join(user_profile, 'AppData', 'Local', 'Microsoft', 'WinGet', 'Packages', 'Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe', 'ffmpeg-7.1.1-full_build', 'bin', 'ffmpeg.exe'),
            os.path.join(local_app_data, 'Microsoft', 'WinGet', 'Packages', 'Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe', 'ffmpeg-7.1.1-full_build', 'bin', 'ffmpeg.exe'),
            r'C:\Users\%USERNAME%\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1.1-full_build\bin\ffmpeg.exe'
        ]
        
        for path in possible_paths:
            if shutil.which(path) or os.path.exists(path):
                self.logger.info("Found FFmpeg at: %s", path)
                return path
                
        self.logger.warning("FFmpeg not found. Please install FFmpeg for audio conversion.")
        return None
        
    def convert_file(self, input_path: str, output_path: str, output_format: str, quality: str = 'high') -> bool:
        """Convert a single audio file"""
        if not self.ffmpeg_path:
            self.logger.error("FFmpeg not available")
            return False
            
        if not os.path.exists(input_path):
            self.logger.error("Input file not found: %s", input_path)
            return False
            
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            cmd = [self.ffmpeg_path, '-i', input_path]
            
            if output_format.lower() in self.quality_settings:
                if quality in self.quality_settings[output_format.lower()]:
                    cmd.extend(self.quality_settings[output_format.lower()][quality])
                    
            cmd.extend(self.get_format_settings(output_format))
            cmd.extend(['-y', output_path])
            
            self.logger.info("Converting: %s -> %s", input_path, output_path)
            self.logger.info("Command: %s", ' '.join(cmd))
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            
            if result.returncode == 0:
                self.logger.info("Successfully converted: %s", os.path.basename(input_path))
                self.logger.info("Output file size: %s bytes", os.path.getsize(output_path) if os.path.exists(output_path) else "File not found")
                return True
            else:
                self.logger.error("Conversion failed with return code %d", result.returncode)
                self.logger.error("FFmpeg stdout: %s", result.stdout)
                self.logger.error("FFmpeg stderr: %s", result.stderr)
                return False
                
        except OSError as e:
            self.logger.error("Error converting %s: %s", input_path, str(e))
            return False
            
    def get_format_settings(self, output_format: str) -> list:
        """Get format-specific FFmpeg settings"""
        format_settings = {
            'mp3': ['-codec:a', 'libmp3lame'],
            'wav': ['-codec:a', 'pcm_s16le'],
            'flac': ['-codec:a', 'flac'],
            'ogg': ['-codec:a', 'libvorbis'],
            'aac': ['-codec:a', 'aac'],
            'm4a': ['-codec:a', 'aac'],
            'wma': ['-codec:a', 'wmav2'],
            'mp4': ['-codec:a', 'aac', '-codec:v', 'libx264'],
            'avi': ['-codec:a', 'libmp3lame', '-codec:v', 'libx264']
        }
        
        return format_settings.get(output_format.lower(), [])

# Custom Progress Bar for the electronic theme
class NeonProgressBar(tk.Frame):
    """Custom progress bar with dynamic electronic styling"""
    
    def __init__(self, parent, theme=None, **kwargs):
        super().__init__(parent, bg=parent.cget('bg'))
        self.progress_var = tk.DoubleVar()
        self.theme = theme if theme else {
            'primary': '#00ff41',
            'bg_dark': '#0a0a0a',
            'bright': '#40ff80',
            'dark': '#00cc33'
        }
        
        # Create custom styled progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Neon.Horizontal.TProgressbar",
            troughcolor=self.theme['bg_dark'],
            background=self.theme['primary'],
            lightcolor=self.theme['bright'],
            darkcolor=self.theme['dark'],
            bordercolor=self.theme['primary'],
            focuscolor='none'
        )
        
        self.progress_bar = ttk.Progressbar(
            self, 
            variable=self.progress_var,
            style="Neon.Horizontal.TProgressbar",
            length=400,
            mode='determinate'
        )
        self.progress_bar.pack(fill='x', pady=2)
        
        # Progress text
        self.progress_text = tk.Label(
            self,
            text="0%",
            font=("Courier", 8, "bold"),
            fg=self.theme['primary'],
            bg=parent.cget('bg')
        )
        self.progress_text.pack()
        
    def set_progress(self, value):
        """Set progress value (0-100)"""
        self.progress_var.set(value)
        self.progress_text.config(text=f"{value:.1f}%")

class GhostKittyConverter:
    def __init__(self):
        self.root = tk.Tk()
        
        # Initialize theme manager and get random theme
        self.theme_manager = ThemeManager()
        self.current_theme = self.theme_manager.get_random_theme()
        
        # Print theme info to console
        print(f"🎨 Loading Theme: {self.current_theme['name']}")
        print(f"🌈 Primary Color: {self.current_theme['primary']}")
        print(f"✨ Secondary Color: {self.current_theme['secondary']}")
        print(f"🎆 Accent Color: {self.current_theme['accent']}")
        
        self.setup_window()
        self.converter = AudioConverter()
        self.setup_gui()
        self.files_to_convert = []
        self.is_converting = False
        
    def setup_window(self):
        """Setup the main window with dynamic theming"""
        self.root.title(f"👻🎵 GHOST KITTY AUDIO CONVERTER 🎵👻 - {self.current_theme['name']}")
        self.root.geometry("1200x800")
        self.root.configure(bg=self.current_theme['bg_dark'])
        self.root.resizable(True, True)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")
        
        # Setup dynamic styling
        self.setup_styling()
        
    def setup_styling(self):
        """Setup dynamic electronic styling for ttk components"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure Combobox style with current theme
        style.configure(
            "Modern.TCombobox",
            fieldbackground=self.current_theme['bg_light'],
            background=self.current_theme['bg_medium'],
            foreground=self.current_theme['primary'],
            bordercolor=self.current_theme['primary'],
            arrowcolor=self.current_theme['primary'],
            insertcolor=self.current_theme['primary']
        )
        
        # Configure Treeview style with current theme
        style.configure(
            "Modern.Treeview",
            background=self.current_theme['bg_medium'],
            foreground=self.current_theme['primary'],
            fieldbackground=self.current_theme['bg_medium'],
            bordercolor=self.current_theme['accent'],
            lightcolor=self.current_theme['accent'],
            darkcolor=self.current_theme['accent']
        )
        
        style.configure(
            "Modern.Treeview.Heading",
            background=self.current_theme['bg_dark'],
            foreground=self.current_theme['secondary'],
            font=("Arial", 10, "bold")
        )
        
        style.map(
            "Modern.Treeview",
            background=[('selected', self.current_theme['dark'])],
            foreground=[('selected', self.current_theme['bright'])]
        )
        
    def create_glow_button(self, parent, text, command, bg_color=None, width=15, height=1):
        """Create a button with dynamic electronic glow styling"""
        if bg_color is None:
            # Get random color from current theme
            bg_color = random.choice(self.current_theme['button_colors'])
            
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 10, "bold"),
            bg=bg_color,
            fg='#000000',
            activebackground=self.current_theme['bright'],
            activeforeground='#000000',
            relief='raised',
            bd=2,
            width=width,
            height=height,
            cursor='hand2'
        )
        return button
        
    def setup_gui(self):
        """Setup the dynamic themed GUI components"""
        # Main container with themed background
        main_frame = tk.Frame(self.root, bg=self.current_theme['bg_dark'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title with dynamic theme colors
        title_frame = tk.Frame(main_frame, bg=self.current_theme['bg_dark'])
        title_frame.pack(fill='x', pady=(0, 30))
        
        title_label = tk.Label(
            title_frame,
            text="👻 GHOST KITTY AUDIO CONVERTER 👻",
            font=("Arial", 24, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_dark']
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text=f"🎵 UNLIMITED BATCH CONVERSION - {self.current_theme['name'].upper()} THEME 🎵",
            font=("Arial", 12),
            fg=self.current_theme['secondary'],
            bg=self.current_theme['bg_dark']
        )
        subtitle_label.pack()
        
        # Theme info label
        theme_info_label = tk.Label(
            title_frame,
            text=f"✨ Current Theme: {self.current_theme['name']} ✨",
            font=("Arial", 10, "italic"),
            fg=self.current_theme['accent'],
            bg=self.current_theme['bg_dark']
        )
        theme_info_label.pack(pady=(5, 0))
        
        # File selection section
        self.setup_file_section(main_frame)
        
        # Format selection section
        self.setup_format_section(main_frame)
        
        # Progress section
        self.setup_progress_section(main_frame)
        
        # Control buttons
        self.setup_control_section(main_frame)
        
        # File list
        self.setup_file_list(main_frame)
        
    def setup_file_section(self, parent):
        """Setup file selection section with dynamic theming"""
        file_frame = tk.LabelFrame(
            parent,
            text="📁 SELECT AUDIO FILES",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=2,
            relief='ridge'
        )
        file_frame.pack(fill='x', pady=(0, 20))
        
        button_frame = tk.Frame(file_frame, bg=self.current_theme['bg_medium'])
        button_frame.pack(pady=15)
        
        # Add files button
        self.add_files_btn = self.create_glow_button(
            button_frame,
            "🎵 ADD FILES",
            self.add_files
        )
        self.add_files_btn.pack(side='left', padx=10)
        
        # Add folder button
        self.add_folder_btn = self.create_glow_button(
            button_frame,
            "📁 ADD FOLDER",
            self.add_folder
        )
        self.add_folder_btn.pack(side='left', padx=10)
        
        # Clear all button
        self.clear_btn = self.create_glow_button(
            button_frame,
            "🗑️ CLEAR ALL",
            self.clear_files
        )
        self.clear_btn.pack(side='left', padx=10)
        
    def setup_format_section(self, parent):
        """Setup format selection section with dynamic theming"""
        format_frame = tk.LabelFrame(
            parent,
            text="🎛️ OUTPUT FORMAT & SETTINGS",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=2,
            relief='ridge'
        )
        format_frame.pack(fill='x', pady=(0, 20))
        
        settings_frame = tk.Frame(format_frame, bg=self.current_theme['bg_medium'])
        settings_frame.pack(pady=15)
        
        # Output format selection
        tk.Label(
            settings_frame,
            text="Output Format:",
            font=("Arial", 10, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium']
        ).grid(row=0, column=0, padx=10, sticky='w')
        
        self.format_var = tk.StringVar(value="mp3")
        format_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.format_var,
            values=["mp3", "wav", "flac", "ogg", "aac", "m4a", "wma", "mp4", "avi"],
            state="readonly",
            width=10,
            font=("Arial", 10),
            style="Modern.TCombobox"
        )
        format_combo.grid(row=0, column=1, padx=10)
        
        # Quality selection
        tk.Label(
            settings_frame,
            text="Quality:",
            font=("Arial", 10, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium']
        ).grid(row=0, column=2, padx=10, sticky='w')
        
        self.quality_var = tk.StringVar(value="high")
        quality_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.quality_var,
            values=["low", "medium", "high", "highest"],
            state="readonly",
            width=10,
            font=("Arial", 10),
            style="Modern.TCombobox"
        )
        quality_combo.grid(row=0, column=3, padx=10)
        
        # Output folder selection
        tk.Label(
            settings_frame,
            text="Output Folder:",
            font=("Arial", 10, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium']
        ).grid(row=1, column=0, padx=10, pady=10, sticky='w')
        
        self.output_folder_var = tk.StringVar(value=str(Path.home() / "Downloads" / "GhostKitty_Converted"))
        self.output_entry = tk.Entry(
            settings_frame,
            textvariable=self.output_folder_var,
            width=40,
            font=("Arial", 10),
            bg=self.current_theme['bg_light'],
            fg=self.current_theme['primary'],
            insertbackground=self.current_theme['primary']
        )
        self.output_entry.grid(row=1, column=1, columnspan=2, padx=10, sticky='ew')
        
        self.browse_output_btn = self.create_glow_button(
            settings_frame,
            "📁 BROWSE",
            self.browse_output_folder,
            width=10
        )
        self.browse_output_btn.grid(row=1, column=3, padx=10)
        
    def setup_progress_section(self, parent):
        """Setup progress tracking section with dynamic theming"""
        progress_frame = tk.LabelFrame(
            parent,
            text="⚡ CONVERSION PROGRESS",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=2,
            relief='ridge'
        )
        progress_frame.pack(fill='x', pady=(0, 20))
        
        # Overall progress
        progress_container = tk.Frame(progress_frame, bg=self.current_theme['bg_medium'])
        progress_container.pack(pady=15, padx=20, fill='x')
        
        self.progress_label = tk.Label(
            progress_container,
            text="Ready to convert...",
            font=("Arial", 10),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium']
        )
        self.progress_label.pack(anchor='w')
        
        self.progress_bar = NeonProgressBar(progress_container, theme=self.current_theme)
        self.progress_bar.pack(fill='x', pady=5)
        
        # Current file info
        self.current_file_label = tk.Label(
            progress_container,
            text="",
            font=("Arial", 8),
            fg=self.current_theme['secondary'],
            bg=self.current_theme['bg_medium']
        )
        self.current_file_label.pack(anchor='w')
        
    def setup_control_section(self, parent):
        """Setup control buttons section with dynamic theming"""
        control_frame = tk.Frame(parent, bg=self.current_theme['bg_dark'])
        control_frame.pack(fill='x', pady=(0, 20))
        
        # Convert button
        self.convert_btn = self.create_glow_button(
            control_frame,
            "🚀 START CONVERSION",
            self.start_conversion,
            width=20,
            height=2
        )
        self.convert_btn.pack(side='left', padx=10)
        
        # Stop button
        self.stop_btn = self.create_glow_button(
            control_frame,
            "🛑 STOP",
            self.stop_conversion,
            width=15,
            height=2
        )
        self.stop_btn.config(state='disabled')
        self.stop_btn.pack(side='left', padx=10)
        
        # Theme change button
        self.theme_btn = self.create_glow_button(
            control_frame,
            "🎨 NEW THEME",
            self.change_theme,
            width=15,
            height=2
        )
        self.theme_btn.pack(side='left', padx=10)
        
        # Stats label
        self.stats_label = tk.Label(
            control_frame,
            text=f"Files: 0 | {self.current_theme['name']} Theme | Ready to rock! 🤘",
            font=("Arial", 10),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_dark']
        )
        self.stats_label.pack(side='right', padx=10)
        
    def setup_file_list(self, parent):
        """Setup file list display with dynamic theming"""
        list_frame = tk.LabelFrame(
            parent,
            text="📋 FILES QUEUE",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=2,
            relief='ridge'
        )
        list_frame.pack(fill='both', expand=True)
        
        # Treeview for file list
        self.tree = ttk.Treeview(
            list_frame,
            columns=('Size', 'Format', 'Status'),
            show='tree headings',
            height=15,
            style="Modern.Treeview"
        )
        
        # Configure columns
        self.tree.heading('#0', text='File Name')
        self.tree.heading('Size', text='Size')
        self.tree.heading('Format', text='Format')
        self.tree.heading('Status', text='Status')
        
        self.tree.column('#0', width=400)
        self.tree.column('Size', width=100)
        self.tree.column('Format', width=80)
        self.tree.column('Status', width=120)
        
        # Scrollbars
        tree_scroll_y = ttk.Scrollbar(list_frame, orient='vertical', command=self.tree.yview)
        tree_scroll_x = ttk.Scrollbar(list_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
        
        # Pack treeview and scrollbars
        self.tree.pack(side='left', fill='both', expand=True, padx=(10, 0), pady=10)
        tree_scroll_y.pack(side='right', fill='y', pady=10)
        tree_scroll_x.pack(side='bottom', fill='x', padx=10)
        
    def add_files(self):
        """Add individual audio files"""
        files = filedialog.askopenfilenames(
            title="Select Audio Files",
            filetypes=[
                ("All Audio", "*.mp3;*.wav;*.flac;*.ogg;*.aac;*.m4a;*.wma;*.mp4;*.avi"),
                ("MP3 files", "*.mp3"),
                ("WAV files", "*.wav"),
                ("FLAC files", "*.flac"),
                ("OGG files", "*.ogg"),
                ("AAC files", "*.aac"),
                ("M4A files", "*.m4a"),
                ("WMA files", "*.wma"),
                ("MP4 files", "*.mp4"),
                ("AVI files", "*.avi"),
                ("All files", "*.*")
            ]
        )
        
        for file_path in files:
            self.add_file_to_queue(file_path)
            
    def add_folder(self):
        """Add all audio files from a folder"""
        folder = filedialog.askdirectory(title="Select Folder with Audio Files")
        if folder:
            audio_extensions = {'.mp3', '.wav', '.flac', '.ogg', '.aac', '.m4a', '.wma', '.mp4', '.avi'}
            
            for root_dir, _, files in os.walk(folder):
                for file in files:
                    if Path(file).suffix.lower() in audio_extensions:
                        file_path = os.path.join(root_dir, file)
                        self.add_file_to_queue(file_path)
                        
    def add_file_to_queue(self, file_path):
        """Add a file to the conversion queue"""
        if file_path not in [f['path'] for f in self.files_to_convert]:
            file_info = {
                'path': file_path,
                'name': Path(file_path).name,
                'size': self.get_file_size(file_path),
                'format': Path(file_path).suffix[1:].upper(),
                'status': 'Waiting'
            }
            
            self.files_to_convert.append(file_info)
            
            # Add to treeview
            self.tree.insert('', 'end', 
                           text=file_info['name'],
                           values=(file_info['size'], file_info['format'], file_info['status']))
            
            self.update_stats()
            
    def get_file_size(self, file_path):
        """Get human readable file size"""
        try:
            size = os.path.getsize(file_path)
            for unit in ['B', 'KB', 'MB', 'GB']:
                if size < 1024:
                    return f"{size:.1f} {unit}"
                size /= 1024
            return f"{size:.1f} TB"
        except OSError:
            return "Unknown"
            
    def clear_files(self):
        """Clear all files from queue"""
        self.files_to_convert.clear()
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.update_stats()
        
    def browse_output_folder(self):
        """Browse for output folder"""
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder_var.set(folder)
            
    def update_stats(self):
        """Update statistics display with theme info"""
        file_count = len(self.files_to_convert)
        self.stats_label.config(text=f"Files: {file_count} | {self.current_theme['name']} Theme | Ready to rock! 🤘")
        
    def change_theme(self):
        """Change to a new random theme"""
        # Get a new random theme
        self.current_theme = self.theme_manager.get_random_theme()
        
        print(f"🎨 Theme Changed: {self.current_theme['name']}")
        print(f"🌈 Primary Color: {self.current_theme['primary']}")
        print(f"✨ Secondary Color: {self.current_theme['secondary']}")
        print(f"🎆 Accent Color: {self.current_theme['accent']}")
        
        # Show theme change message
        messagebox.showinfo(
            "Theme Changed", 
            f"🎨 New Theme Applied: {self.current_theme['name']}\n\n"
            f"🌈 Primary: {self.current_theme['primary']}\n"
            f"✨ Secondary: {self.current_theme['secondary']}\n"
            f"🎆 Accent: {self.current_theme['accent']}\n\n"
            "Restart the app to see the full theme change!"
        )
        
        # Update window title
        self.root.title(f"👻🎵 GHOST KITTY AUDIO CONVERTER 🎵👻 - {self.current_theme['name']}")
        
        # Update some colors that can be changed immediately
        self.stats_label.config(fg=self.current_theme['primary'])
        self.update_stats()
        
    def start_conversion(self):
        """Start the batch conversion process"""
        if not self.files_to_convert:
            messagebox.showwarning("No Files", "Please add some audio files first!")
            return
            
        if self.is_converting:
            return
            
        # Create output directory
        output_dir = Path(self.output_folder_var.get())
        output_dir.mkdir(parents=True, exist_ok=True)
        
        self.is_converting = True
        self.convert_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
        # Start conversion in separate thread
        self.conversion_thread = threading.Thread(target=self.convert_files)
        self.conversion_thread.daemon = True
        self.conversion_thread.start()
        
    def convert_files(self):
        """Convert all files in the queue"""
        total_files = len(self.files_to_convert)
        
        for i, file_info in enumerate(self.files_to_convert):
            if not self.is_converting:
                break
                
            # Update progress
            progress = (i / total_files) * 100
            self.root.after(0, self.update_progress, progress, f"Converting {file_info['name']}...")
            
            # Update file status in tree
            for item in self.tree.get_children():
                if self.tree.item(item, 'text') == file_info['name']:
                    self.tree.set(item, 'Status', 'Converting...')
                    break
            
            try:
                # Convert the file
                input_path = file_info['path']
                output_format = self.format_var.get()
                quality = self.quality_var.get()
                output_dir = Path(self.output_folder_var.get())
                
                output_filename = f"{Path(input_path).stem}.{output_format}"
                output_path = output_dir / output_filename
                
                success = self.converter.convert_file(input_path, str(output_path), output_format, quality)
                
                # Update status
                status = "✅ Completed" if success else "❌ Failed"
                for item in self.tree.get_children():
                    if self.tree.item(item, 'text') == file_info['name']:
                        self.tree.set(item, 'Status', status)
                        break
                        
            except Exception as e:
                # Update status on error
                for item in self.tree.get_children():
                    if self.tree.item(item, 'text') == file_info['name']:
                        self.tree.set(item, 'Status', f"❌ Error: {str(e)[:20]}")
                        break
        
        # Conversion complete
        if self.is_converting:
            self.root.after(0, self.update_progress, 100, "🎉 All conversions completed!")
            self.root.after(0, self.conversion_finished)
        
    def update_progress(self, progress, message):
        """Update progress bar and labels"""
        self.progress_bar.set_progress(progress)
        self.progress_label.config(text=message)
        if "Converting" in message:
            self.current_file_label.config(text=message)
        
    def conversion_finished(self):
        """Handle conversion completion"""
        self.is_converting = False
        self.convert_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        messagebox.showinfo("Conversion Complete", "🎉 All files have been converted successfully!")
        
    def stop_conversion(self):
        """Stop the conversion process"""
        self.is_converting = False
        self.convert_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.progress_label.config(text="Conversion stopped by user")
        
    def run(self):
        """Start the application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = GhostKittyConverter()
    app.run()
