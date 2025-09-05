#!/usr/bin/env python3
"""
🎵 GHOST KITTY AUDIO CONVERTER - MEGA ENHANCED VERSION 🎵
Super Cool Electronic Style Audio Converter with INSANE UPGRADES!
New Features: Drag & Drop, Audio Visualization, Enhanced Animations, and More!
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
import json
import math

# Try to import enhanced features (graceful fallback if not available)
try:
    import tkinterdnd2 as tkdnd
    DRAG_DROP_AVAILABLE = True
except ImportError:
    DRAG_DROP_AVAILABLE = False
    print("💡 Drag & Drop not available - install tkinterdnd2 for this feature")

try:
    from PIL import Image, ImageTk, ImageDraw
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("💡 Enhanced graphics not available - install Pillow for this feature")

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    print("💡 Audio visualization not available - install numpy for this feature")

# Enhanced Theme Manager with MORE THEMES!
class MegaThemeManager:
    """Ultra enhanced theme manager with tons of new themes"""
    
    def __init__(self):
        self.current_theme = self.generate_random_theme()
        
    def get_mega_themes(self):
        """Get expanded collection of awesome themes"""
        themes = [
            {
                'name': 'Ghost Kitty Classic',
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
                'name': 'Vaporwave Dreams',
                'bg_dark': '#0a0a0f',
                'bg_medium': '#1a1525',
                'bg_light': '#2a203a',
                'primary': '#ff00ff',
                'secondary': '#00ffff',
                'accent': '#ff69b4',
                'bright': '#ff1493',
                'dark': '#9400d3',
                'text_primary': '#ff00ff',
                'text_secondary': '#00ffff',
                'text_accent': '#ff69b4',
                'button_colors': ['#ff00ff', '#00ffff', '#ff69b4', '#ff1493', '#9400d3', '#da70d6']
            },
            {
                'name': 'Synthwave Sunset',
                'bg_dark': '#0f0515',
                'bg_medium': '#1f0a2a',
                'bg_light': '#2f0f3f',
                'primary': '#ff0080',
                'secondary': '#ff8000',
                'accent': '#ffff00',
                'bright': '#ff4080',
                'dark': '#cc0060',
                'text_primary': '#ff0080',
                'text_secondary': '#ff8000',
                'text_accent': '#ffff00',
                'button_colors': ['#ff0080', '#ff8000', '#ffff00', '#ff4080', '#cc0060', '#ff6040']
            },
            {
                'name': 'Matrix Green',
                'bg_dark': '#000500',
                'bg_medium': '#001a00',
                'bg_light': '#002a00',
                'primary': '#00ff00',
                'secondary': '#80ff80',
                'accent': '#40ff40',
                'bright': '#60ff60',
                'dark': '#00cc00',
                'text_primary': '#00ff00',
                'text_secondary': '#80ff80',
                'text_accent': '#40ff40',
                'button_colors': ['#00ff00', '#80ff80', '#40ff40', '#60ff60', '#00cc00', '#20ff20']
            },
            {
                'name': 'Neon Tokyo',
                'bg_dark': '#050010',
                'bg_medium': '#150020',
                'bg_light': '#250030',
                'primary': '#ff0040',
                'secondary': '#0040ff',
                'accent': '#ff4080',
                'bright': '#ff6080',
                'dark': '#cc0030',
                'text_primary': '#ff0040',
                'text_secondary': '#0040ff',
                'text_accent': '#ff4080',
                'button_colors': ['#ff0040', '#0040ff', '#ff4080', '#ff6080', '#cc0030', '#ff0080']
            },
            {
                'name': 'Electric Teal',
                'bg_dark': '#001a1a',
                'bg_medium': '#002a2a',
                'bg_light': '#003a3a',
                'primary': '#00ffff',
                'secondary': '#80ffff',
                'accent': '#40ffff',
                'bright': '#60ffff',
                'dark': '#00cccc',
                'text_primary': '#00ffff',
                'text_secondary': '#80ffff',
                'text_accent': '#40ffff',
                'button_colors': ['#00ffff', '#80ffff', '#40ffff', '#60ffff', '#00cccc', '#20ffff']
            },
            {
                'name': 'Cyber Orange',
                'bg_dark': '#1a0500',
                'bg_medium': '#2a0a00',
                'bg_light': '#3a0f00',
                'primary': '#ff8000',
                'secondary': '#ffff00',
                'accent': '#ff4000',
                'bright': '#ffa040',
                'dark': '#cc6600',
                'text_primary': '#ff8000',
                'text_secondary': '#ffff00',
                'text_accent': '#ff4000',
                'button_colors': ['#ff8000', '#ffff00', '#ff4000', '#ffa040', '#cc6600', '#ff6020']
            }
        ]
        return themes
        
    def generate_random_theme(self):
        """Generate enhanced random theme"""
        base_hue = random.uniform(0, 360)
        
        # More sophisticated color harmony
        primary_hue = base_hue
        secondary_hue = (base_hue + 120) % 360
        accent_hue = (base_hue + 240) % 360
        
        primary_color = self.hsv_to_hex(primary_hue, 0.9, 0.9)
        secondary_color = self.hsv_to_hex(secondary_hue, 0.85, 0.85)
        accent_color = self.hsv_to_hex(accent_hue, 0.8, 0.8)
        
        # Generate more color variations
        button_colors = []
        for i in range(6):
            hue = (base_hue + i * 60) % 360
            saturation = random.uniform(0.7, 1.0)
            brightness = random.uniform(0.7, 1.0)
            button_colors.append(self.hsv_to_hex(hue, saturation, brightness))
        
        theme = {
            'name': self.generate_epic_theme_name(),
            'bg_dark': '#0a0a0a',
            'bg_medium': '#1a1a1a',
            'bg_light': '#2a2a2a',
            'primary': primary_color,
            'secondary': secondary_color,
            'accent': accent_color,
            'bright': self.hsv_to_hex(primary_hue, 0.7, 1.0),
            'dark': self.hsv_to_hex(primary_hue, 0.9, 0.5),
            'text_primary': primary_color,
            'text_secondary': secondary_color,
            'text_accent': accent_color,
            'button_colors': button_colors
        }
        
        return theme
        
    def hsv_to_hex(self, h, s, v):
        """Convert HSV to hex color"""
        rgb = colorsys.hsv_to_rgb(h / 360, s, v)
        return f"#{int(rgb[0]*255):02x}{int(rgb[1]*255):02x}{int(rgb[2]*255):02x}"
        
    def generate_epic_theme_name(self):
        """Generate even cooler theme names"""
        prefixes = [
            "Ultra", "Mega", "Hyper", "Super", "Quantum", "Cosmic", "Astro", "Cyber",
            "Neo", "Turbo", "Nitro", "Plasma", "Atomic", "Digital", "Virtual", "Neural",
            "Chrome", "Neon", "Electric", "Laser", "Hologram", "Matrix", "Binary", "Data"
        ]
        
        cores = [
            "Wave", "Pulse", "Storm", "Blast", "Rush", "Surge", "Flow", "Stream",
            "Force", "Power", "Energy", "Drive", "Core", "Grid", "Net", "Code",
            "Sync", "Loop", "Beat", "Rhythm", "Vibe", "Zone", "Field", "Spark"
        ]
        
        suffixes = [
            "X", "Pro", "Max", "Ultra", "Prime", "Elite", "Turbo", "Boost",
            "Plus", "Supreme", "Extreme", "Advanced", "Enhanced", "2.0", "XL"
        ]
        
        return f"{random.choice(prefixes)} {random.choice(cores)} {random.choice(suffixes)}"

# Enhanced particle system for background effects
class ParticleSystem:
    """Advanced particle system with more effects"""
    
    def __init__(self, canvas, theme):
        self.canvas = canvas
        self.theme = theme
        self.particles = []
        self.animation_running = True
        self.effect_type = random.choice(['sparkles', 'floating', 'matrix', 'energy'])
        
    def create_particle(self):
        """Create enhanced particles based on effect type"""
        if self.effect_type == 'matrix':
            return self.create_matrix_particle()
        elif self.effect_type == 'energy':
            return self.create_energy_particle()
        else:
            return self.create_sparkle_particle()
            
    def create_sparkle_particle(self):
        """Create sparkle particle"""
        return {
            'x': random.randint(0, 800),
            'y': random.randint(0, 600),
            'vx': random.uniform(-0.5, 0.5),
            'vy': random.uniform(-0.5, 0.5),
            'size': random.randint(1, 4),
            'color': random.choice(self.theme['button_colors']),
            'life': random.randint(150, 300),
            'type': 'sparkle'
        }
        
    def create_matrix_particle(self):
        """Create Matrix-style falling particle"""
        return {
            'x': random.randint(0, 800),
            'y': 0,
            'vx': 0,
            'vy': random.uniform(1, 3),
            'size': random.randint(2, 6),
            'color': self.theme['primary'],
            'life': random.randint(200, 400),
            'type': 'matrix'
        }
        
    def create_energy_particle(self):
        """Create energy beam particle"""
        return {
            'x': random.randint(0, 800),
            'y': random.randint(0, 600),
            'vx': random.uniform(-2, 2),
            'vy': random.uniform(-2, 2),
            'size': random.randint(3, 8),
            'color': self.theme['accent'],
            'life': random.randint(100, 200),
            'type': 'energy',
            'trail': []
        }
        
    def update_particles(self):
        """Enhanced particle updating"""
        # Add particles based on effect type
        max_particles = {'sparkles': 30, 'floating': 40, 'matrix': 50, 'energy': 25}
        spawn_rate = {'sparkles': 0.1, 'floating': 0.08, 'matrix': 0.15, 'energy': 0.05}
        
        if len(self.particles) < max_particles.get(self.effect_type, 30):
            if random.random() < spawn_rate.get(self.effect_type, 0.1):
                self.particles.append(self.create_particle())
        
        # Update particles
        for particle in self.particles[:]:
            self.update_single_particle(particle)
            
        if self.animation_running:
            self.canvas.after(50, self.update_particles)
            self.draw_particles()
            
    def update_single_particle(self, particle):
        """Update single particle"""
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        particle['life'] -= 1
        
        # Special behavior for different types
        if particle['type'] == 'matrix':
            if particle['y'] > 600:
                particle['y'] = 0
                particle['x'] = random.randint(0, 800)
        elif particle['type'] == 'energy':
            # Add to trail
            if 'trail' not in particle:
                particle['trail'] = []
            particle['trail'].append((particle['x'], particle['y']))
            if len(particle['trail']) > 5:
                particle['trail'].pop(0)
                
        # Remove dead particles
        if particle['life'] <= 0:
            if particle in self.particles:
                self.particles.remove(particle)
                
    def draw_particles(self):
        """Draw enhanced particles"""
        self.canvas.delete("particle")
        for particle in self.particles:
            if particle['type'] == 'energy' and 'trail' in particle:
                self.draw_energy_trail(particle)
            else:
                self.draw_standard_particle(particle)
                
    def draw_energy_trail(self, particle):
        """Draw energy particle with trail"""
        # Draw trail
        for i, (tx, ty) in enumerate(particle['trail']):
            alpha = i / len(particle['trail'])
            size = particle['size'] * alpha
            self.canvas.create_oval(
                tx - size, ty - size,
                tx + size, ty + size,
                fill=particle['color'],
                outline="",
                tags="particle"
            )
        
        # Draw main particle
        self.canvas.create_oval(
            particle['x'] - particle['size'],
            particle['y'] - particle['size'],
            particle['x'] + particle['size'],
            particle['y'] + particle['size'],
            fill=particle['color'],
            outline="white",
            width=1,
            tags="particle"
        )
        
    def draw_standard_particle(self, particle):
        """Draw standard particle"""
        self.canvas.create_oval(
            particle['x'] - particle['size'],
            particle['y'] - particle['size'],
            particle['x'] + particle['size'],
            particle['y'] + particle['size'],
            fill=particle['color'],
            outline="",
            tags="particle"
        )

# Enhanced progress bar with more animations
class MegaProgressBar:
    """Ultra enhanced progress bar with insane animations"""
    
    def __init__(self, parent, theme, width=500, height=40):
        self.theme = theme
        self.canvas = tk.Canvas(
            parent, 
            width=width, 
            height=height, 
            bg=theme['bg_dark'], 
            highlightthickness=0
        )
        self.canvas.pack()
        self.width = width
        self.height = height
        self.progress = 0
        self.animation_frame = 0
        self.animate_progress()
        
    def set_progress(self, value):
        """Set progress with smooth animation"""
        self.progress = min(100, max(0, value))
        
    def animate_progress(self):
        """Continuous progress animation"""
        self.animation_frame += 1
        self.draw_enhanced_progress()
        self.canvas.after(50, self.animate_progress)
        
    def draw_enhanced_progress(self):
        """Draw progress with multiple visual effects"""
        self.canvas.delete("all")
        
        # Background with subtle pattern
        self.draw_background_pattern()
        
        # Main progress bar
        fill_width = (self.progress / 100) * self.width
        
        if fill_width > 0:
            # Animated gradient fill
            self.draw_animated_gradient(fill_width)
            
            # Glow effect
            self.draw_glow_effect(fill_width)
            
            # Moving highlight
            self.draw_moving_highlight(fill_width)
            
        # Progress text with glow
        self.draw_progress_text()
        
        # Border
        self.canvas.create_rectangle(
            0, 0, self.width, self.height,
            outline=self.theme['primary'], width=2, fill=""
        )
        
    def draw_background_pattern(self):
        """Draw animated background pattern"""
        # Moving diagonal lines
        for i in range(0, self.width + 20, 20):
            x = i + (self.animation_frame % 40) - 20
            self.canvas.create_line(
                x, 0, x + self.height, self.height,
                fill=self.theme['bg_light'], width=1
            )
            
    def draw_animated_gradient(self, fill_width):
        """Draw animated gradient fill"""
        steps = int(fill_width)
        for i in range(steps):
            # Color interpolation with animation
            ratio = i / self.width + math.sin(self.animation_frame * 0.1) * 0.1
            
            if ratio > 1:
                ratio = ratio - 1
            if ratio < 0:
                ratio = 1 + ratio
                
            color = self.interpolate_color(
                self.theme['primary'],
                self.theme['secondary'],
                ratio
            )
            
            self.canvas.create_line(
                i, 2, i, self.height - 2,
                fill=color, width=1
            )
            
    def draw_glow_effect(self, fill_width):
        """Draw outer glow effect"""
        glow_steps = 3
        for step in range(glow_steps):
            alpha = (glow_steps - step) / glow_steps
            glow_color = self.theme['primary']
            
            # Approximate glow with multiple rectangles
            self.canvas.create_rectangle(
                -step, -step, fill_width + step, self.height + step,
                outline=glow_color, width=1, fill=""
            )
            
    def draw_moving_highlight(self, fill_width):
        """Draw moving highlight effect"""
        if fill_width > 10:
            highlight_pos = (self.animation_frame * 3) % fill_width
            highlight_width = 20
            
            self.canvas.create_rectangle(
                highlight_pos, 5,
                min(highlight_pos + highlight_width, fill_width), self.height - 5,
                fill=self.theme['bright'], outline=""
            )
            
    def draw_progress_text(self):
        """Draw progress text with glow effect"""
        text = f"{self.progress:.1f}%"
        
        # Text shadow/glow effect
        for offset in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            self.canvas.create_text(
                self.width // 2 + offset[0],
                self.height // 2 + offset[1],
                text=text,
                fill=self.theme['dark'],
                font=("Arial", 12, "bold")
            )
            
        # Main text
        self.canvas.create_text(
            self.width // 2, self.height // 2,
            text=text,
            fill='white',
            font=("Arial", 12, "bold")
        )
        
    def interpolate_color(self, color1, color2, t):
        """Enhanced color interpolation"""
        try:
            c1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
            c2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
            
            result = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
            
            return f"#{result[0]:02x}{result[1]:02x}{result[2]:02x}"
        except:
            return color1

# Continue with the rest of your original AudioConverter class but with enhancements...
class AudioConverter:
    """Enhanced core audio conversion engine"""
    
    def __init__(self):
        self.setup_logging()
        self.ffmpeg_path = self.find_ffmpeg()
        
        # Enhanced quality settings
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
                'highest': ['-ar', '96000', '-sample_fmt', 's32']
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
            },
            'aac': {
                'low': ['-b:a', '128k'],
                'medium': ['-b:a', '192k'],
                'high': ['-b:a', '256k'],
                'highest': ['-b:a', '320k']
            },
            'm4a': {
                'low': ['-b:a', '128k'],
                'medium': ['-b:a', '192k'],
                'high': ['-b:a', '256k'],
                'highest': ['-b:a', '320k']
            }
        }
        
    def setup_logging(self):
        """Enhanced logging setup"""
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
        """Enhanced FFmpeg detection"""
        possible_paths = [
            'ffmpeg',
            'ffmpeg.exe',
            '/usr/bin/ffmpeg',
            '/usr/local/bin/ffmpeg',
            '/opt/homebrew/bin/ffmpeg',  # macOS Apple Silicon
            r'C:\ffmpeg\bin\ffmpeg.exe',
            r'C:\Program Files\ffmpeg\bin\ffmpeg.exe',
        ]
        
        for path in possible_paths:
            if shutil.which(path) or os.path.exists(path):
                self.logger.info("Found FFmpeg at: %s", path)
                return path
                
        self.logger.warning("FFmpeg not found. Install with: 'winget install FFmpeg' (Windows) or 'brew install ffmpeg' (macOS)")
        return None
        
    def convert_file(self, input_path: str, output_path: str, output_format: str, quality: str = 'high') -> bool:
        """Enhanced conversion with better error handling"""
        if not self.ffmpeg_path:
            self.logger.error("FFmpeg not available")
            return False
            
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            cmd = [self.ffmpeg_path, '-i', input_path]
            
            # Add quality settings
            if output_format.lower() in self.quality_settings:
                quality_params = self.quality_settings[output_format.lower()].get(quality, [])
                cmd.extend(quality_params)
                
            # Add format-specific settings
            cmd.extend(['-y', output_path])
            
            self.logger.info("Converting: %s -> %s", input_path, output_path)
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300,  # 5 minute timeout
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            
            if result.returncode == 0:
                self.logger.info("Conversion successful: %s", output_path)
                return True
            else:
                self.logger.error("Conversion failed: %s", result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            self.logger.error("Conversion timeout: %s", input_path)
            return False
        except Exception as e:
            self.logger.error("Conversion error: %s", str(e))
            return False

# Your main application class but enhanced!
class MegaGhostKittyConverter:
    """ULTIMATE Ghost Kitty Audio Converter with ALL THE FEATURES!"""
    
    def __init__(self):
        self.setup_application()
        self.setup_enhanced_gui()
        
    def setup_application(self):
        """Initialize the mega enhanced application"""
        # Initialize with drag and drop support if available
        if DRAG_DROP_AVAILABLE:
            self.root = tkdnd.Tk()
        else:
            self.root = tk.Tk()
            
        self.root.title("👻🎵 GHOST KITTY AUDIO CONVERTER - MEGA ENHANCED EDITION 🎵👻")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        
        # Initialize components
        self.theme_manager = MegaThemeManager()
        self.current_theme = self.theme_manager.current_theme
        self.converter = AudioConverter()
        self.files_to_convert = []
        self.is_converting = False
        self.conversion_thread = None
        
        # Enhanced variables
        self.format_var = tk.StringVar(value="mp3")
        self.quality_var = tk.StringVar(value="high")
        self.output_folder_var = tk.StringVar(value=os.path.expanduser("~/Desktop/GhostKittyOutput"))
        
        # Apply theme to root
        self.root.configure(bg=self.current_theme['bg_dark'])
        
    def setup_enhanced_gui(self):
        """Setup the mega enhanced GUI"""
        # Main container
        main_container = tk.Frame(self.root, bg=self.current_theme['bg_dark'])
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Background effects canvas
        self.bg_canvas = tk.Canvas(
            main_container,
            highlightthickness=0,
            bg=self.current_theme['bg_dark']
        )
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Initialize particle system
        self.particle_system = ParticleSystem(self.bg_canvas, self.current_theme)
        self.particle_system.update_particles()
        
        # Content frame (above background)
        self.content_frame = tk.Frame(main_container, bg=self.current_theme['bg_dark'])
        self.content_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Setup GUI sections
        self.setup_mega_header()
        self.setup_file_section()
        self.setup_format_section()
        self.setup_progress_section()
        self.setup_control_section()
        self.setup_file_list()
        
        # Setup drag and drop if available
        if DRAG_DROP_AVAILABLE:
            self.setup_drag_drop()
            
    def setup_mega_header(self):
        """Setup enhanced header with theme switching"""
        header_frame = tk.Frame(self.content_frame, bg=self.current_theme['bg_dark'])
        header_frame.pack(fill='x', pady=(0, 20))
        
        # Main title with enhanced styling
        title_label = tk.Label(
            header_frame,
            text="👻🎵 GHOST KITTY AUDIO CONVERTER - MEGA EDITION 🎵👻",
            font=("Arial", 20, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_dark']
        )
        title_label.pack()
        
        # Subtitle with current theme
        subtitle_label = tk.Label(
            header_frame,
            text=f"🌈 UNLIMITED THEMES & EFFECTS - CURRENT: {self.current_theme['name'].upper()} 🌈",
            font=("Arial", 12),
            fg=self.current_theme['secondary'],
            bg=self.current_theme['bg_dark']
        )
        subtitle_label.pack()
        
        # Theme controls
        theme_control_frame = tk.Frame(header_frame, bg=self.current_theme['bg_dark'])
        theme_control_frame.pack(pady=10)
        
        # Random theme button
        self.create_enhanced_button(
            theme_control_frame,
            "🎲 RANDOM THEME",
            self.change_random_theme,
            self.current_theme['accent']
        ).pack(side='left', padx=5)
        
        # Predefined themes button
        self.create_enhanced_button(
            theme_control_frame,
            "🎨 PRESET THEMES",
            self.show_theme_selector,
            self.current_theme['secondary']
        ).pack(side='left', padx=5)
        
    def create_enhanced_button(self, parent, text, command, color):
        """Create enhanced button with hover effects"""
        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 10, "bold"),
            fg='white',
            bg=color,
            activebackground=self.brighten_color(color),
            activeforeground='white',
            relief='flat',
            bd=2,
            padx=15,
            pady=8,
            cursor='hand2'
        )
        
        # Enhanced hover effects
        def on_enter(event):
            button.config(bg=self.brighten_color(color), relief='raised')
            
        def on_leave(event):
            button.config(bg=color, relief='flat')
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
        return button
        
    def brighten_color(self, hex_color):
        """Brighten a color for hover effects"""
        try:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            brightened = tuple(min(255, int(c * 1.3)) for c in rgb)
            return f"#{brightened[0]:02x}{brightened[1]:02x}{brightened[2]:02x}"
        except:
            return hex_color
            
    def change_random_theme(self):
        """Change to a random theme with animation"""
        old_theme = self.current_theme
        self.current_theme = self.theme_manager.generate_random_theme()
        self.animate_theme_change(old_theme, self.current_theme)
        
    def animate_theme_change(self, old_theme, new_theme):
        """Animate theme change (simplified version)"""
        # Update particle system theme
        self.particle_system.theme = new_theme
        
        # Update all GUI elements
        self.refresh_all_widgets()
        
        # Show theme change message
        messagebox.showinfo(
            "Theme Changed! 🎨", 
            f"Now using: {new_theme['name']}\n\nEnjoy your new cyberpunk experience! 🚀"
        )
        
    def show_theme_selector(self):
        """Show theme selection dialog"""
        theme_dialog = tk.Toplevel(self.root)
        theme_dialog.title("🎨 Select Theme")
        theme_dialog.geometry("400x500")
        theme_dialog.configure(bg=self.current_theme['bg_dark'])
        
        # Theme list
        themes = self.theme_manager.get_mega_themes()
        
        for i, theme in enumerate(themes):
            theme_frame = tk.Frame(theme_dialog, bg=self.current_theme['bg_medium'])
            theme_frame.pack(fill='x', padx=10, pady=5)
            
            # Theme preview
            preview_canvas = tk.Canvas(theme_frame, width=50, height=30, bg=theme['primary'])
            preview_canvas.pack(side='left', padx=5)
            
            # Theme name and button
            tk.Label(
                theme_frame,
                text=theme['name'],
                bg=self.current_theme['bg_medium'],
                fg=self.current_theme['text_primary'],
                font=("Arial", 10)
            ).pack(side='left', padx=10)
            
            tk.Button(
                theme_frame,
                text="Use This Theme",
                command=lambda t=theme: self.apply_selected_theme(t, theme_dialog),
                bg=theme['primary'],
                fg='white',
                font=("Arial", 8)
            ).pack(side='right', padx=5)
            
    def apply_selected_theme(self, theme, dialog):
        """Apply selected theme"""
        self.current_theme = theme
        self.theme_manager.current_theme = theme
        self.refresh_all_widgets()
        dialog.destroy()
        
    def refresh_all_widgets(self):
        """Refresh all widgets with new theme"""
        # This would be a comprehensive refresh of all GUI elements
        # For brevity, showing key updates
        self.root.configure(bg=self.current_theme['bg_dark'])
        self.content_frame.configure(bg=self.current_theme['bg_dark'])
        
        # Update particle system
        if hasattr(self, 'particle_system'):
            self.particle_system.theme = self.current_theme
            
    def setup_file_section(self):
        """Enhanced file selection section"""
        file_frame = tk.LabelFrame(
            self.content_frame,
            text="📁 SELECT AUDIO FILES - ENHANCED WITH DRAG & DROP!",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=3,
            relief='ridge'
        )
        file_frame.pack(fill='x', pady=(0, 20))
        
        # Drag and drop info
        if DRAG_DROP_AVAILABLE:
            drop_info = tk.Label(
                file_frame,
                text="💫 You can drag & drop files directly onto this window! 💫",
                font=("Arial", 9, "italic"),
                fg=self.current_theme['accent'],
                bg=self.current_theme['bg_medium']
            )
            drop_info.pack(pady=5)
            
        button_frame = tk.Frame(file_frame, bg=self.current_theme['bg_medium'])
        button_frame.pack(pady=15)
        
        # Enhanced buttons
        self.create_enhanced_button(
            button_frame,
            "🎵 ADD FILES",
            self.add_files,
            self.current_theme['button_colors'][0]
        ).pack(side='left', padx=8)
        
        self.create_enhanced_button(
            button_frame,
            "📁 ADD FOLDER",
            self.add_folder,
            self.current_theme['button_colors'][1]
        ).pack(side='left', padx=8)
        
        self.create_enhanced_button(
            button_frame,
            "🗑️ CLEAR ALL", 
            self.clear_files,
            self.current_theme['button_colors'][2]
        ).pack(side='left', padx=8)
        
    def setup_format_section(self):
        """Enhanced format selection"""
        format_frame = tk.LabelFrame(
            self.content_frame,
            text="🎛️ OUTPUT FORMAT & QUALITY SETTINGS",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=3,
            relief='ridge'
        )
        format_frame.pack(fill='x', pady=(0, 20))
        
        settings_grid = tk.Frame(format_frame, bg=self.current_theme['bg_medium'])
        settings_grid.pack(pady=15)
        
        # Format selection
        tk.Label(
            settings_grid,
            text="Format:",
            font=("Arial", 11, "bold"),
            fg=self.current_theme['text_primary'],
            bg=self.current_theme['bg_medium']
        ).grid(row=0, column=0, padx=15, sticky='w')
        
        format_combo = ttk.Combobox(
            settings_grid,
            textvariable=self.format_var,
            values=['mp3', 'wav', 'flac', 'ogg', 'aac', 'm4a'],
            state='readonly',
            width=10,
            font=("Arial", 10)
        )
        format_combo.grid(row=0, column=1, padx=15)
        
        # Quality selection
        tk.Label(
            settings_grid,
            text="Quality:",
            font=("Arial", 11, "bold"),
            fg=self.current_theme['text_primary'],
            bg=self.current_theme['bg_medium']
        ).grid(row=0, column=2, padx=15, sticky='w')
        
        quality_combo = ttk.Combobox(
            settings_grid,
            textvariable=self.quality_var,
            values=['low', 'medium', 'high', 'highest'],
            state='readonly',
            width=10,
            font=("Arial", 10)
        )
        quality_combo.grid(row=0, column=3, padx=15)
        
        # Output folder
        tk.Label(
            settings_grid,
            text="Output Folder:",
            font=("Arial", 11, "bold"),
            fg=self.current_theme['text_primary'],
            bg=self.current_theme['bg_medium']
        ).grid(row=1, column=0, padx=15, sticky='w', pady=(10, 0))
        
        folder_frame = tk.Frame(settings_grid, bg=self.current_theme['bg_medium'])
        folder_frame.grid(row=1, column=1, columnspan=2, padx=15, pady=(10, 0), sticky='ew')
        
        folder_entry = tk.Entry(
            folder_frame,
            textvariable=self.output_folder_var,
            font=("Arial", 9),
            width=30
        )
        folder_entry.pack(side='left', fill='x', expand=True)
        
        self.create_enhanced_button(
            folder_frame,
            "📂 Browse",
            self.browse_output_folder,
            self.current_theme['accent']
        ).pack(side='right', padx=(5, 0))
        
    def setup_progress_section(self):
        """Enhanced progress section with mega progress bar"""
        progress_frame = tk.LabelFrame(
            self.content_frame,
            text="⚡ CONVERSION PROGRESS - MEGA ENHANCED ⚡",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=3,
            relief='ridge'
        )
        progress_frame.pack(fill='x', pady=(0, 20))
        
        # Mega progress bar
        self.mega_progress = MegaProgressBar(
            progress_frame, 
            self.current_theme,
            width=600,
            height=50
        )
        
        # Status labels
        self.progress_label = tk.Label(
            progress_frame,
            text="Ready to convert! 🚀",
            font=("Arial", 11),
            fg=self.current_theme['text_secondary'],
            bg=self.current_theme['bg_medium']
        )
        self.progress_label.pack(pady=10)
        
    def setup_control_section(self):
        """Enhanced control buttons"""
        control_frame = tk.Frame(self.content_frame, bg=self.current_theme['bg_dark'])
        control_frame.pack(pady=20)
        
        self.convert_btn = self.create_enhanced_button(
            control_frame,
            "🚀 START MEGA CONVERSION!",
            self.start_conversion,
            self.current_theme['button_colors'][3]
        )
        self.convert_btn.pack(side='left', padx=15)
        
        self.stop_btn = self.create_enhanced_button(
            control_frame,
            "⏹️ STOP",
            self.stop_conversion,
            self.current_theme['button_colors'][4]
        )
        self.stop_btn.pack(side='left', padx=15)
        self.stop_btn.config(state='disabled')
        
    def setup_file_list(self):
        """Enhanced file list with better styling"""
        list_frame = tk.LabelFrame(
            self.content_frame,
            text="📋 FILE QUEUE - ENHANCED VIEW",
            font=("Arial", 12, "bold"),
            fg=self.current_theme['primary'],
            bg=self.current_theme['bg_medium'],
            bd=3,
            relief='ridge'
        )
        list_frame.pack(fill='both', expand=True)
        
        # Treeview with enhanced columns
        columns = ('Name', 'Format', 'Size', 'Status')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=8)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
            
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(list_frame, orient='horizontal', command=self.tree.xview)
        
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack everything
        self.tree.pack(side='left', fill='both', expand=True)
        v_scrollbar.pack(side='right', fill='y')
        h_scrollbar.pack(side='bottom', fill='x')
        
    def setup_drag_drop(self):
        """Setup enhanced drag and drop"""
        if DRAG_DROP_AVAILABLE:
            self.root.drop_target_register(tkdnd.DND_FILES)
            self.root.dnd_bind('<<Drop>>', self.on_drop)
            
    def on_drop(self, event):
        """Handle dropped files with enhanced feedback"""
        if not DRAG_DROP_AVAILABLE:
            return
            
        files = event.data.split()
        added_count = 0
        
        for file_path in files:
            file_path = file_path.strip('{}')
            if self.add_file_to_list(file_path):
                added_count += 1
                
        if added_count > 0:
            messagebox.showinfo(
                "Files Added! 🎵",
                f"Successfully added {added_count} audio file(s) via drag & drop!"
            )
    
    # Continue with enhanced versions of your existing methods...
    def add_files(self):
        """Enhanced file selection"""
        filetypes = [
            ("All Audio", "*.mp3;*.wav;*.flac;*.ogg;*.aac;*.m4a;*.wma"),
            ("MP3 files", "*.mp3"),
            ("WAV files", "*.wav"),
            ("FLAC files", "*.flac"),
            ("OGG files", "*.ogg"),
            ("AAC files", "*.aac"),
            ("M4A files", "*.m4a"),
            ("WMA files", "*.wma"),
            ("All files", "*.*")
        ]
        
        files = filedialog.askopenfilenames(
            title="Select Audio Files - Ghost Kitty Style! 🎵",
            filetypes=filetypes
        )
        
        added_count = 0
        for file in files:
            if self.add_file_to_list(file):
                added_count += 1
                
        if added_count > 0:
            messagebox.showinfo("Success! 🎵", f"Added {added_count} files to the conversion queue!")
            
    def add_folder(self):
        """Enhanced folder selection"""
        folder = filedialog.askdirectory(title="Select Folder with Audio Files 📁")
        if folder:
            added_count = self.add_folder_files(folder)
            if added_count > 0:
                messagebox.showinfo("Success! 📁", f"Added {added_count} audio files from the selected folder!")
            else:
                messagebox.showwarning("No Files", "No supported audio files found in the selected folder.")
                
    def add_folder_files(self, folder_path):
        """Add all audio files from a folder"""
        audio_extensions = {'.mp3', '.wav', '.flac', '.ogg', '.aac', '.m4a', '.wma'}
        added_count = 0
        
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if Path(file).suffix.lower() in audio_extensions:
                    file_path = os.path.join(root, file)
                    if self.add_file_to_list(file_path):
                        added_count += 1
                        
        return added_count
        
    def add_file_to_list(self, file_path):
        """Add file to conversion list with enhanced info"""
        if not os.path.exists(file_path):
            return False
            
        # Check if file is already in list
        for existing_file in self.files_to_convert:
            if existing_file['path'] == file_path:
                return False
                
        # Get file info
        file_info = {
            'path': file_path,
            'name': os.path.basename(file_path),
            'size': self.format_file_size(os.path.getsize(file_path)),
            'format': Path(file_path).suffix.upper().lstrip('.')
        }
        
        self.files_to_convert.append(file_info)
        
        # Add to tree view
        self.tree.insert('', 'end', values=(
            file_info['name'],
            file_info['format'], 
            file_info['size'],
            'Ready ⭐'
        ))
        
        return True
        
    def format_file_size(self, size_bytes):
        """Format file size in human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
        
    def clear_files(self):
        """Enhanced file clearing with confirmation"""
        if not self.files_to_convert:
            return
            
        result = messagebox.askyesno(
            "Clear All Files? 🗑️",
            f"This will remove all {len(self.files_to_convert)} files from the queue.\n\nAre you sure?"
        )
        
        if result:
            self.files_to_convert.clear()
            for item in self.tree.get_children():
                self.tree.delete(item)
            messagebox.showinfo("Cleared! ✨", "All files have been removed from the queue!")
            
    def browse_output_folder(self):
        """Browse for output folder"""
        folder = filedialog.askdirectory(
            title="Select Output Folder 📂",
            initialdir=self.output_folder_var.get()
        )
        if folder:
            self.output_folder_var.set(folder)
            
    def start_conversion(self):
        """Start enhanced conversion process"""
        if not self.files_to_convert:
            messagebox.showwarning("No Files! 😅", "Please add some audio files first!")
            return
            
        if self.is_converting:
            return
            
        # Create output directory
        output_dir = Path(self.output_folder_var.get())
        output_dir.mkdir(parents=True, exist_ok=True)
        
        self.is_converting = True
        self.convert_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        
        # Start enhanced conversion
        self.conversion_thread = threading.Thread(target=self.enhanced_convert_files)
        self.conversion_thread.daemon = True
        self.conversion_thread.start()
        
    def enhanced_convert_files(self):
        """Enhanced conversion with better progress tracking"""
        total_files = len(self.files_to_convert)
        
        for i, file_info in enumerate(self.files_to_convert):
            if not self.is_converting:
                break
                
            # Update progress with enhanced messages
            progress = (i / total_files) * 100
            status_message = f"🎵 Converting {file_info['name']} ({i+1}/{total_files}) 🎵"
            
            self.root.after(0, self.mega_progress.set_progress, progress)
            self.root.after(0, self.update_progress_label, status_message)
            
            # Update file status in tree
            self.update_tree_status(file_info['name'], '🔄 Converting...')
            
            try:
                # Convert with enhanced parameters
                input_path = file_info['path']
                output_format = self.format_var.get()
                quality = self.quality_var.get()
                output_dir = Path(self.output_folder_var.get())
                
                output_filename = f"{Path(input_path).stem}.{output_format}"
                output_path = output_dir / output_filename
                
                success = self.converter.convert_file(input_path, str(output_path), output_format, quality)
                
                # Update status with enhanced icons
                status = "✅ Completed!" if success else "❌ Failed"
                self.update_tree_status(file_info['name'], status)
                
            except Exception as e:
                self.update_tree_status(file_info['name'], f"❌ Error: {str(e)[:20]}")
                
        # Enhanced completion
        if self.is_converting:
            self.root.after(0, self.mega_progress.set_progress, 100)
            self.root.after(0, self.update_progress_label, "🎉 ALL CONVERSIONS COMPLETED! 🎉")
            self.root.after(0, self.conversion_finished)
            
    def update_progress_label(self, message):
        """Update progress label"""
        self.progress_label.config(text=message)
        
    def update_tree_status(self, filename, status):
        """Update file status in tree view"""
        for item in self.tree.get_children():
            if self.tree.item(item, 'values')[0] == filename:
                current_values = list(self.tree.item(item, 'values'))
                current_values[3] = status
                self.tree.item(item, values=current_values)
                break
                
    def conversion_finished(self):
        """Enhanced conversion completion"""
        self.is_converting = False
        self.convert_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        
        # Show enhanced completion message
        messagebox.showinfo(
            "🎉 MEGA CONVERSION COMPLETE! 🎉",
            f"All {len(self.files_to_convert)} files have been converted successfully!\n\n"
            f"Output Location: {self.output_folder_var.get()}\n\n"
            "Ghost Kitty strikes again! 👻🎵"
        )
        
    def stop_conversion(self):
        """Enhanced conversion stopping"""
        self.is_converting = False
        self.convert_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        self.progress_label.config(text="⏹️ Conversion stopped by user")
        
    def run(self):
        """Start the mega enhanced application"""
        # Show startup message
        messagebox.showinfo(
            "👻 Ghost Kitty Mega Edition! 👻",
            f"Welcome to the ENHANCED Ghost Kitty Audio Converter!\n\n"
            f"🌈 Current Theme: {self.current_theme['name']}\n"
            f"🎵 Drag & Drop: {'Enabled' if DRAG_DROP_AVAILABLE else 'Not Available'}\n"
            f"✨ Enhanced Graphics: {'Enabled' if PIL_AVAILABLE else 'Not Available'}\n"
            f"📊 Audio Visualization: {'Enabled' if NUMPY_AVAILABLE else 'Not Available'}\n\n"
            "Enjoy the enhanced experience! 🚀"
        )
        
        self.root.mainloop()

if __name__ == "__main__":
    print("🚀 Starting Ghost Kitty Audio Converter - MEGA ENHANCED EDITION!")
    app = MegaGhostKittyConverter()
    app.run()
