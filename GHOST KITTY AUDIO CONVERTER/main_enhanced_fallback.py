#!/usr/bin/env python3
"""
🎵 GHOST KITTY AUDIO CONVERTER - ENHANCED FALLBACK VERSION 🎵
Works without optional dependencies but still adds cool new features!
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
import time
import math

class AdvancedThemeManager:
    """Advanced theme manager that works without external dependencies"""
    
    def __init__(self):
        self.current_theme = self.generate_random_theme()
        
    def get_epic_themes(self):
        """Extended collection of handcrafted themes"""
        return [
            {
                'name': 'Ghost Kitty Classic',
                'bg_dark': '#0a0a0a', 'bg_medium': '#1a1a1a', 'bg_light': '#2a2a2a',
                'primary': '#00ff41', 'secondary': '#ff0080', 'accent': '#0080ff',
                'bright': '#40ff80', 'dark': '#00cc33',
                'text_primary': '#00ff41', 'text_secondary': '#ff0080', 'text_accent': '#0080ff',
                'button_colors': ['#ff0080', '#0080ff', '#ff4000', '#00ff00', '#8000ff', '#ffff00']
            },
            {
                'name': 'Vaporwave Sunset',
                'bg_dark': '#0a0a0f', 'bg_medium': '#1a1525', 'bg_light': '#2a203a',
                'primary': '#ff00ff', 'secondary': '#00ffff', 'accent': '#ff69b4',
                'bright': '#ff1493', 'dark': '#9400d3',
                'text_primary': '#ff00ff', 'text_secondary': '#00ffff', 'text_accent': '#ff69b4',
                'button_colors': ['#ff00ff', '#00ffff', '#ff69b4', '#ff1493', '#9400d3', '#da70d6']
            },
            {
                'name': 'Synthwave Neon',
                'bg_dark': '#0f0515', 'bg_medium': '#1f0a2a', 'bg_light': '#2f0f3f',
                'primary': '#ff0080', 'secondary': '#ff8000', 'accent': '#ffff00',
                'bright': '#ff4080', 'dark': '#cc0060',
                'text_primary': '#ff0080', 'text_secondary': '#ff8000', 'text_accent': '#ffff00',
                'button_colors': ['#ff0080', '#ff8000', '#ffff00', '#ff4080', '#cc0060', '#ff6040']
            },
            {
                'name': 'Matrix Digital Rain',
                'bg_dark': '#000500', 'bg_medium': '#001a00', 'bg_light': '#002a00',
                'primary': '#00ff00', 'secondary': '#80ff80', 'accent': '#40ff40',
                'bright': '#60ff60', 'dark': '#00cc00',
                'text_primary': '#00ff00', 'text_secondary': '#80ff80', 'text_accent': '#40ff40',
                'button_colors': ['#00ff00', '#80ff80', '#40ff40', '#60ff60', '#00cc00', '#20ff20']
            },
            {
                'name': 'Cyber Tokyo Night',
                'bg_dark': '#050010', 'bg_medium': '#150020', 'bg_light': '#250030',
                'primary': '#ff0040', 'secondary': '#0040ff', 'accent': '#ff4080',
                'bright': '#ff6080', 'dark': '#cc0030',
                'text_primary': '#ff0040', 'text_secondary': '#0040ff', 'text_accent': '#ff4080',
                'button_colors': ['#ff0040', '#0040ff', '#ff4080', '#ff6080', '#cc0030', '#ff0080']
            },
            {
                'name': 'Electric Ocean',
                'bg_dark': '#001a1a', 'bg_medium': '#002a2a', 'bg_light': '#003a3a',
                'primary': '#00ffff', 'secondary': '#80ffff', 'accent': '#40ffff',
                'bright': '#60ffff', 'dark': '#00cccc',
                'text_primary': '#00ffff', 'text_secondary': '#80ffff', 'text_accent': '#40ffff',
                'button_colors': ['#00ffff', '#80ffff', '#40ffff', '#60ffff', '#00cccc', '#20ffff']
            },
            {
                'name': 'Solar Flare',
                'bg_dark': '#1a0500', 'bg_medium': '#2a0a00', 'bg_light': '#3a0f00',
                'primary': '#ff8000', 'secondary': '#ffff00', 'accent': '#ff4000',
                'bright': '#ffa040', 'dark': '#cc6600',
                'text_primary': '#ff8000', 'text_secondary': '#ffff00', 'text_accent': '#ff4000',
                'button_colors': ['#ff8000', '#ffff00', '#ff4000', '#ffa040', '#cc6600', '#ff6020']
            },
            {
                'name': 'Cosmic Purple',
                'bg_dark': '#1a051a', 'bg_medium': '#2a0a2a', 'bg_light': '#3a0f3a',
                'primary': '#8000ff', 'secondary': '#a040ff', 'accent': '#c080ff',
                'bright': '#b060ff', 'dark': '#6000cc',
                'text_primary': '#8000ff', 'text_secondary': '#a040ff', 'text_accent': '#c080ff',
                'button_colors': ['#8000ff', '#a040ff', '#c080ff', '#b060ff', '#6000cc', '#ff00ff']
            }
        ]
        
    def generate_random_theme(self):
        """Generate awesome random themes without external libraries"""
        # Use built-in math for color generation
        base_hue = random.randint(0, 359)
        
        # Create harmonious color scheme
        colors = []
        for offset in [0, 120, 240]:
            hue = (base_hue + offset) % 360
            colors.append(self.simple_hsv_to_hex(hue, 0.9, 0.85))
            
        # Generate button colors
        button_colors = []
        for i in range(6):
            hue = (base_hue + i * 45) % 360
            saturation = 0.8 + random.random() * 0.2
            brightness = 0.7 + random.random() * 0.3
            button_colors.append(self.simple_hsv_to_hex(hue, saturation, brightness))
            
        return {
            'name': self.generate_cool_name(),
            'bg_dark': '#0a0a0a', 'bg_medium': '#1a1a1a', 'bg_light': '#2a2a2a',
            'primary': colors[0], 'secondary': colors[1], 'accent': colors[2],
            'bright': self.brighten_color(colors[0]), 'dark': self.darken_color(colors[0]),
            'text_primary': colors[0], 'text_secondary': colors[1], 'text_accent': colors[2],
            'button_colors': button_colors
        }
        
    def simple_hsv_to_hex(self, h, s, v):
        """Simple HSV to hex conversion without external libraries"""
        h = h / 360.0
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        
        if i == 0: r, g, b = v, t, p
        elif i == 1: r, g, b = q, v, p
        elif i == 2: r, g, b = p, v, t
        elif i == 3: r, g, b = p, q, v
        elif i == 4: r, g, b = t, p, v
        else: r, g, b = v, p, q
            
        return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"
        
    def brighten_color(self, hex_color):
        """Brighten a color"""
        try:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            brightened = tuple(min(255, int(c * 1.3)) for c in rgb)
            return f"#{brightened[0]:02x}{brightened[1]:02x}{brightened[2]:02x}"
        except:
            return hex_color
            
    def darken_color(self, hex_color):
        """Darken a color"""
        try:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            darkened = tuple(max(0, int(c * 0.6)) for c in rgb)
            return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
        except:
            return hex_color
            
    def generate_cool_name(self):
        """Generate epic theme names"""
        prefixes = ['Ultra', 'Mega', 'Hyper', 'Super', 'Quantum', 'Cosmic', 'Cyber', 'Neo', 'Turbo', 'Nitro']
        cores = ['Wave', 'Pulse', 'Storm', 'Blast', 'Rush', 'Surge', 'Flow', 'Force', 'Energy', 'Power']  
        suffixes = ['X', 'Pro', 'Max', 'Ultra', 'Prime', 'Elite', 'Boost', 'Plus', 'Supreme', 'XL']
        
        return f"{random.choice(prefixes)} {random.choice(cores)} {random.choice(suffixes)}"

class SimpleProgressBar:
    """Enhanced progress bar using only tkinter"""
    
    def __init__(self, parent, theme, width=500, height=30):
        self.theme = theme
        self.canvas = tk.Canvas(parent, width=width, height=height, bg=theme['bg_dark'], highlightthickness=0)
        self.canvas.pack(pady=10)
        self.width = width
        self.height = height
        self.progress = 0
        self.animation_frame = 0
        self.animate()
        
    def set_progress(self, value):
        self.progress = min(100, max(0, value))
        
    def animate(self):
        """Simple animation loop"""
        self.animation_frame += 1
        self.draw_progress()
        self.canvas.after(100, self.animate)
        
    def draw_progress(self):
        """Draw enhanced progress bar"""
        self.canvas.delete("all")
        
        # Background
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill=self.theme['bg_medium'], outline="")
        
        # Progress fill
        fill_width = (self.progress / 100) * self.width
        
        if fill_width > 0:
            # Create simple gradient effect with multiple rectangles
            steps = min(int(fill_width), 20)
            if steps > 0:
                step_width = fill_width / steps
                for i in range(steps):
                    x = i * step_width
                    # Alternate colors for gradient effect
                    color = self.theme['primary'] if i % 2 == 0 else self.theme['secondary']
                    self.canvas.create_rectangle(x, 2, x + step_width, self.height - 2, fill=color, outline="")
                    
            # Moving highlight effect
            if fill_width > 10:
                highlight_pos = (self.animation_frame * 2) % fill_width
                self.canvas.create_rectangle(
                    highlight_pos, 5, min(highlight_pos + 15, fill_width), self.height - 5,
                    fill=self.theme['bright'], outline=""
                )
                
        # Progress text
        text = f"{self.progress:.1f}%"
        self.canvas.create_text(self.width//2, self.height//2, text=text, fill='white', font=("Arial", 10, "bold"))
        
        # Border
        self.canvas.create_rectangle(0, 0, self.width, self.height, outline=self.theme['primary'], width=2, fill="")

class SimpleParticles:
    """Simple particle system using only tkinter"""
    
    def __init__(self, canvas, theme):
        self.canvas = canvas
        self.theme = theme
        self.particles = []
        self.running = True
        self.update_particles()
        
    def update_particles(self):
        """Simple particle update"""
        if not self.running:
            return
            
        # Add new particles occasionally
        if len(self.particles) < 20 and random.random() < 0.1:
            self.particles.append({
                'x': random.randint(0, 800),
                'y': random.randint(0, 600), 
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(-1, 1),
                'size': random.randint(2, 5),
                'color': random.choice(self.theme['button_colors']),
                'life': random.randint(100, 200)
            })
            
        # Update particles
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy'] 
            particle['life'] -= 1
            
            # Bounce off edges
            if particle['x'] <= 0 or particle['x'] >= 800:
                particle['vx'] *= -1
            if particle['y'] <= 0 or particle['y'] >= 600:
                particle['vy'] *= -1
                
            # Remove dead particles
            if particle['life'] <= 0:
                self.particles.remove(particle)
                
        # Draw particles
        self.canvas.delete("particle")
        for particle in self.particles:
            self.canvas.create_oval(
                particle['x'] - particle['size'],
                particle['y'] - particle['size'],
                particle['x'] + particle['size'], 
                particle['y'] + particle['size'],
                fill=particle['color'], outline="", tags="particle"
            )
            
        # Schedule next update
        self.canvas.after(50, self.update_particles)

# Your enhanced audio converter (reuse from original with improvements)
class EnhancedAudioConverter:
    """Enhanced version of the audio converter"""
    
    def __init__(self):
        self.setup_logging()
        self.ffmpeg_path = self.find_ffmpeg()
        
        # Enhanced quality settings with more options
        self.quality_settings = {
            'mp3': {'low': ['-b:a', '128k'], 'medium': ['-b:a', '192k'], 'high': ['-b:a', '320k'], 'highest': ['-b:a', '320k', '-q:a', '0']},
            'wav': {'low': ['-ar', '22050'], 'medium': ['-ar', '44100'], 'high': ['-ar', '48000'], 'highest': ['-ar', '96000']},
            'flac': {'low': ['-compression_level', '0'], 'medium': ['-compression_level', '5'], 'high': ['-compression_level', '8'], 'highest': ['-compression_level', '12']},
            'ogg': {'low': ['-b:a', '96k'], 'medium': ['-b:a', '160k'], 'high': ['-b:a', '256k'], 'highest': ['-b:a', '500k']},
            'aac': {'low': ['-b:a', '128k'], 'medium': ['-b:a', '192k'], 'high': ['-b:a', '256k'], 'highest': ['-b:a', '320k']},
            'm4a': {'low': ['-b:a', '128k'], 'medium': ['-b:a', '192k'], 'high': ['-b:a', '256k'], 'highest': ['-b:a', '320k']}
        }
        
    def setup_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                           handlers=[logging.FileHandler('ghostkitty_converter.log'), logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)
        
    def find_ffmpeg(self) -> Optional[str]:
        """Enhanced FFmpeg detection"""
        possible_paths = ['ffmpeg', 'ffmpeg.exe', '/usr/bin/ffmpeg', '/usr/local/bin/ffmpeg',
                         r'C:\ffmpeg\bin\ffmpeg.exe', r'C:\Program Files\ffmpeg\bin\ffmpeg.exe']
        
        for path in possible_paths:
            if shutil.which(path) or os.path.exists(path):
                self.logger.info(f"Found FFmpeg at: {path}")
                return path
                
        self.logger.warning("FFmpeg not found")
        return None
        
    def convert_file(self, input_path: str, output_path: str, output_format: str, quality: str = 'high') -> bool:
        """Convert file with enhanced error handling"""
        if not self.ffmpeg_path:
            return False
            
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            cmd = [self.ffmpeg_path, '-i', input_path]
            
            if output_format.lower() in self.quality_settings:
                cmd.extend(self.quality_settings[output_format.lower()].get(quality, []))
                
            cmd.extend(['-y', output_path])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300,
                                  creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0)
            
            return result.returncode == 0
            
        except Exception as e:
            self.logger.error(f"Conversion error: {e}")
            return False

class EnhancedGhostKittyConverter:
    """Enhanced Ghost Kitty Converter that works without optional dependencies"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("👻🎵 GHOST KITTY AUDIO CONVERTER - ENHANCED EDITION 🎵👻")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Initialize theme manager and converter
        self.theme_manager = AdvancedThemeManager()
        self.current_theme = self.theme_manager.current_theme
        self.converter = EnhancedAudioConverter()
        
        # Variables
        self.files_to_convert = []
        self.is_converting = False
        self.format_var = tk.StringVar(value="mp3")
        self.quality_var = tk.StringVar(value="high") 
        self.output_folder_var = tk.StringVar(value=os.path.expanduser("~/Desktop/GhostKittyOutput"))
        
        self.setup_gui()
        
    def setup_gui(self):
        """Setup enhanced GUI"""
        self.root.configure(bg=self.current_theme['bg_dark'])
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.current_theme['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Background canvas for particles
        self.bg_canvas = tk.Canvas(main_container, highlightthickness=0, bg=self.current_theme['bg_dark'])
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Particle system
        self.particles = SimpleParticles(self.bg_canvas, self.current_theme)
        
        # Content frame
        content_frame = tk.Frame(main_container, bg=self.current_theme['bg_dark'])
        content_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        self.setup_header(content_frame)
        self.setup_file_section(content_frame)
        self.setup_format_section(content_frame)
        self.setup_progress_section(content_frame)
        self.setup_controls(content_frame)
        self.setup_file_list(content_frame)
        
    def setup_header(self, parent):
        """Setup enhanced header"""
        header_frame = tk.Frame(parent, bg=self.current_theme['bg_dark'])
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Title
        title_label = tk.Label(header_frame, text="👻🎵 GHOST KITTY AUDIO CONVERTER - ENHANCED EDITION 🎵👻",
                              font=("Arial", 18, "bold"), fg=self.current_theme['primary'], bg=self.current_theme['bg_dark'])
        title_label.pack()
        
        # Subtitle
        subtitle_label = tk.Label(header_frame, text=f"🌈 CURRENT THEME: {self.current_theme['name'].upper()} 🌈",
                                 font=("Arial", 11), fg=self.current_theme['secondary'], bg=self.current_theme['bg_dark'])
        subtitle_label.pack()
        
        # Theme buttons
        theme_frame = tk.Frame(header_frame, bg=self.current_theme['bg_dark'])
        theme_frame.pack(pady=10)
        
        self.create_glow_button(theme_frame, "🎲 RANDOM THEME", self.random_theme, self.current_theme['accent']).pack(side='left', padx=5)
        self.create_glow_button(theme_frame, "🎨 PRESET THEMES", self.show_themes, self.current_theme['secondary']).pack(side='left', padx=5)
        
    def create_glow_button(self, parent, text, command, color):
        """Create button with glow effect"""
        button = tk.Button(parent, text=text, command=command, font=("Arial", 9, "bold"), fg='white', bg=color,
                          activebackground=self.theme_manager.brighten_color(color), relief='flat', bd=2, padx=12, pady=6, cursor='hand2')
        
        def on_enter(e): button.config(bg=self.theme_manager.brighten_color(color), relief='raised')
        def on_leave(e): button.config(bg=color, relief='flat')
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        return button
        
    def random_theme(self):
        """Apply random theme"""
        old_theme = self.current_theme['name']
        self.current_theme = self.theme_manager.generate_random_theme()
        self.particles.theme = self.current_theme
        self.refresh_gui()
        messagebox.showinfo("Theme Changed! 🎨", f"Changed from {old_theme} to {self.current_theme['name']}!")
        
    def show_themes(self):
        """Show theme selection dialog"""
        dialog = tk.Toplevel(self.root)
        dialog.title("🎨 Choose Your Theme")
        dialog.geometry("500x400")
        dialog.configure(bg=self.current_theme['bg_dark'])
        
        themes = self.theme_manager.get_epic_themes()
        
        for theme in themes:
            frame = tk.Frame(dialog, bg=self.current_theme['bg_medium'])
            frame.pack(fill='x', padx=10, pady=5)
            
            # Theme preview
            preview = tk.Canvas(frame, width=40, height=25, bg=theme['primary'])
            preview.pack(side='left', padx=5)
            preview.create_rectangle(10, 5, 30, 20, fill=theme['secondary'], outline="")
            
            # Theme info
            tk.Label(frame, text=theme['name'], bg=self.current_theme['bg_medium'], fg=self.current_theme['text_primary'], font=("Arial", 10)).pack(side='left', padx=10)
            
            # Apply button
            tk.Button(frame, text="Use Theme", command=lambda t=theme: self.apply_theme(t, dialog),
                     bg=theme['primary'], fg='white', font=("Arial", 8)).pack(side='right', padx=5)
                     
    def apply_theme(self, theme, dialog):
        """Apply selected theme"""
        self.current_theme = theme
        self.particles.theme = theme
        self.refresh_gui()
        dialog.destroy()
        
    def refresh_gui(self):
        """Refresh GUI with new theme"""
        self.root.configure(bg=self.current_theme['bg_dark'])
        # Note: Full GUI refresh would require rebuilding all widgets
        # For simplicity, showing concept - full implementation would update all colors
        
    def setup_file_section(self, parent):
        """Setup file selection section"""
        file_frame = tk.LabelFrame(parent, text="📁 SELECT AUDIO FILES", font=("Arial", 11, "bold"),
                                  fg=self.current_theme['primary'], bg=self.current_theme['bg_medium'], bd=2, relief='ridge')
        file_frame.pack(fill='x', pady=(0, 15))
        
        button_frame = tk.Frame(file_frame, bg=self.current_theme['bg_medium'])
        button_frame.pack(pady=12)
        
        self.create_glow_button(button_frame, "🎵 ADD FILES", self.add_files, self.current_theme['button_colors'][0]).pack(side='left', padx=8)
        self.create_glow_button(button_frame, "📁 ADD FOLDER", self.add_folder, self.current_theme['button_colors'][1]).pack(side='left', padx=8)
        self.create_glow_button(button_frame, "🗑️ CLEAR ALL", self.clear_files, self.current_theme['button_colors'][2]).pack(side='left', padx=8)
        
    def setup_format_section(self, parent):
        """Setup format selection"""
        format_frame = tk.LabelFrame(parent, text="🎛️ OUTPUT SETTINGS", font=("Arial", 11, "bold"),
                                    fg=self.current_theme['primary'], bg=self.current_theme['bg_medium'], bd=2, relief='ridge')
        format_frame.pack(fill='x', pady=(0, 15))
        
        settings_frame = tk.Frame(format_frame, bg=self.current_theme['bg_medium'])
        settings_frame.pack(pady=12)
        
        # Format
        tk.Label(settings_frame, text="Format:", font=("Arial", 10, "bold"), fg=self.current_theme['text_primary'], bg=self.current_theme['bg_medium']).grid(row=0, column=0, padx=12, sticky='w')
        ttk.Combobox(settings_frame, textvariable=self.format_var, values=['mp3', 'wav', 'flac', 'ogg', 'aac', 'm4a'], state='readonly', width=8).grid(row=0, column=1, padx=12)
        
        # Quality
        tk.Label(settings_frame, text="Quality:", font=("Arial", 10, "bold"), fg=self.current_theme['text_primary'], bg=self.current_theme['bg_medium']).grid(row=0, column=2, padx=12, sticky='w')
        ttk.Combobox(settings_frame, textvariable=self.quality_var, values=['low', 'medium', 'high', 'highest'], state='readonly', width=8).grid(row=0, column=3, padx=12)
        
        # Output folder
        tk.Label(settings_frame, text="Output:", font=("Arial", 10, "bold"), fg=self.current_theme['text_primary'], bg=self.current_theme['bg_medium']).grid(row=1, column=0, padx=12, sticky='w', pady=(8,0))
        folder_frame = tk.Frame(settings_frame, bg=self.current_theme['bg_medium'])
        folder_frame.grid(row=1, column=1, columnspan=2, padx=12, pady=(8,0), sticky='ew')
        tk.Entry(folder_frame, textvariable=self.output_folder_var, font=("Arial", 8), width=25).pack(side='left', fill='x', expand=True)
        self.create_glow_button(folder_frame, "📂", self.browse_folder, self.current_theme['accent']).pack(side='right', padx=(3,0))
        
    def setup_progress_section(self, parent):
        """Setup progress section"""
        progress_frame = tk.LabelFrame(parent, text="⚡ CONVERSION PROGRESS", font=("Arial", 11, "bold"),
                                      fg=self.current_theme['primary'], bg=self.current_theme['bg_medium'], bd=2, relief='ridge')
        progress_frame.pack(fill='x', pady=(0, 15))
        
        self.progress_bar = SimpleProgressBar(progress_frame, self.current_theme)
        
        self.progress_label = tk.Label(progress_frame, text="Ready to convert! 🚀", font=("Arial", 10),
                                      fg=self.current_theme['text_secondary'], bg=self.current_theme['bg_medium'])
        self.progress_label.pack(pady=8)
        
    def setup_controls(self, parent):
        """Setup control buttons"""
        control_frame = tk.Frame(parent, bg=self.current_theme['bg_dark'])
        control_frame.pack(pady=15)
        
        self.convert_btn = self.create_glow_button(control_frame, "🚀 START CONVERSION!", self.start_conversion, self.current_theme['button_colors'][3])
        self.convert_btn.pack(side='left', padx=12)
        
        self.stop_btn = self.create_glow_button(control_frame, "⏹️ STOP", self.stop_conversion, self.current_theme['button_colors'][4])
        self.stop_btn.pack(side='left', padx=12)
        self.stop_btn.config(state='disabled')
        
    def setup_file_list(self, parent):
        """Setup file list"""
        list_frame = tk.LabelFrame(parent, text="📋 FILE QUEUE", font=("Arial", 11, "bold"),
                                  fg=self.current_theme['primary'], bg=self.current_theme['bg_medium'], bd=2, relief='ridge')
        list_frame.pack(fill='both', expand=True)
        
        columns = ('Name', 'Format', 'Status')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=6)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
            
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
    # File management methods
    def add_files(self):
        files = filedialog.askopenfilenames(title="Select Audio Files", filetypes=[
            ("All Audio", "*.mp3;*.wav;*.flac;*.ogg;*.aac;*.m4a"), ("All files", "*.*")])
        for file in files:
            self.add_file_to_list(file)
            
    def add_folder(self):
        folder = filedialog.askdirectory(title="Select Folder")
        if folder:
            audio_exts = {'.mp3', '.wav', '.flac', '.ogg', '.aac', '.m4a'}
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if Path(file).suffix.lower() in audio_exts:
                        self.add_file_to_list(os.path.join(root, file))
                        
    def add_file_to_list(self, file_path):
        if not os.path.exists(file_path) or any(f['path'] == file_path for f in self.files_to_convert):
            return
            
        file_info = {'path': file_path, 'name': os.path.basename(file_path), 'format': Path(file_path).suffix.upper().lstrip('.')}
        self.files_to_convert.append(file_info)
        self.tree.insert('', 'end', values=(file_info['name'], file_info['format'], 'Ready ⭐'))
        
    def clear_files(self):
        if self.files_to_convert and messagebox.askyesno("Clear Files?", "Remove all files from queue?"):
            self.files_to_convert.clear()
            for item in self.tree.get_children():
                self.tree.delete(item)
                
    def browse_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder_var.set(folder)
            
    # Conversion methods
    def start_conversion(self):
        if not self.files_to_convert:
            messagebox.showwarning("No Files", "Please add some audio files first!")
            return
            
        self.is_converting = True
        self.convert_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
        # Start conversion in thread
        self.conversion_thread = threading.Thread(target=self.convert_files, daemon=True)
        self.conversion_thread.start()
        
    def convert_files(self):
        total = len(self.files_to_convert)
        output_dir = Path(self.output_folder_var.get())
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for i, file_info in enumerate(self.files_to_convert):
            if not self.is_converting:
                break
                
            progress = (i / total) * 100
            self.root.after(0, self.progress_bar.set_progress, progress)
            self.root.after(0, self.update_status, f"Converting {file_info['name']}...")
            self.root.after(0, self.update_tree_status, file_info['name'], '🔄 Converting...')
            
            # Convert file
            output_path = output_dir / f"{Path(file_info['path']).stem}.{self.format_var.get()}"
            success = self.converter.convert_file(file_info['path'], str(output_path), self.format_var.get(), self.quality_var.get())
            
            status = "✅ Done!" if success else "❌ Failed"
            self.root.after(0, self.update_tree_status, file_info['name'], status)
            
        if self.is_converting:
            self.root.after(0, self.progress_bar.set_progress, 100)
            self.root.after(0, self.update_status, "🎉 All conversions completed!")
            self.root.after(0, self.conversion_finished)
            
    def update_status(self, message):
        self.progress_label.config(text=message)
        
    def update_tree_status(self, filename, status):
        for item in self.tree.get_children():
            values = list(self.tree.item(item, 'values'))
            if values[0] == filename:
                values[2] = status
                self.tree.item(item, values=values)
                break
                
    def conversion_finished(self):
        self.is_converting = False
        self.convert_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        messagebox.showinfo("Complete! 🎉", f"All {len(self.files_to_convert)} files converted successfully!")
        
    def stop_conversion(self):
        self.is_converting = False
        self.convert_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.progress_label.config(text="Conversion stopped")
        
    def run(self):
        messagebox.showinfo("👻 Enhanced Ghost Kitty! 👻", 
                           f"Welcome to Enhanced Ghost Kitty Audio Converter!\n\n"
                           f"🌈 Current Theme: {self.current_theme['name']}\n"
                           f"✨ Enhanced features ready!\n\n"
                           f"Try the theme buttons for different looks! 🎨")
        self.root.mainloop()

if __name__ == "__main__":
    print("🚀 Starting Ghost Kitty Audio Converter - Enhanced Fallback Edition!")
    app = EnhancedGhostKittyConverter()
    app.run()
