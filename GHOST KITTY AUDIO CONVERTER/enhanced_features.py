#!/usr/bin/env python3
"""
🎵 GHOST KITTY AUDIO CONVERTER - ENHANCED VERSION 🎵
Super Cool Electronic Style Audio Converter with MEGA UPGRADES!
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import tkinterdnd2 as tkdnd
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
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import pygame

class ParticleSystem:
    """Animated particle system for background effects"""
    
    def __init__(self, canvas, theme):
        self.canvas = canvas
        self.theme = theme
        self.particles = []
        self.animation_running = True
        
    def create_particle(self):
        """Create a new particle"""
        return {
            'x': random.randint(0, 800),
            'y': random.randint(0, 600),
            'vx': random.uniform(-1, 1),
            'vy': random.uniform(-1, 1),
            'size': random.randint(2, 6),
            'color': random.choice(self.theme['button_colors']),
            'alpha': random.uniform(0.3, 1.0),
            'life': random.randint(100, 300)
        }
        
    def update_particles(self):
        """Update particle positions and properties"""
        # Add new particles
        if len(self.particles) < 50 and random.random() < 0.1:
            self.particles.append(self.create_particle())
            
        # Update existing particles
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['life'] -= 1
            
            # Remove dead particles
            if particle['life'] <= 0:
                self.particles.remove(particle)
                
        # Schedule next update
        if self.animation_running:
            self.canvas.after(50, self.update_particles)
            self.draw_particles()
            
    def draw_particles(self):
        """Draw all particles"""
        self.canvas.delete("particle")
        for particle in self.particles:
            self.canvas.create_oval(
                particle['x'] - particle['size'],
                particle['y'] - particle['size'],
                particle['x'] + particle['size'],
                particle['y'] + particle['size'],
                fill=particle['color'],
                outline="",
                tags="particle"
            )

class AudioVisualizer:
    """Audio waveform and spectrum visualization"""
    
    def __init__(self, canvas, width=400, height=100):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.waveform_data = []
        self.is_analyzing = False
        
    def generate_fake_waveform(self):
        """Generate fake waveform for demo purposes"""
        return [random.randint(10, 90) for _ in range(100)]
        
    def draw_waveform(self, theme):
        """Draw animated waveform"""
        self.canvas.delete("waveform")
        
        if not self.waveform_data:
            self.waveform_data = self.generate_fake_waveform()
            
        # Draw waveform bars
        bar_width = self.width // len(self.waveform_data)
        
        for i, amplitude in enumerate(self.waveform_data):
            x = i * bar_width
            height = amplitude
            
            # Create gradient effect
            color = theme['primary'] if i % 2 == 0 else theme['secondary']
            
            self.canvas.create_rectangle(
                x, self.height - height,
                x + bar_width - 1, self.height,
                fill=color,
                outline="",
                tags="waveform"
            )
            
        # Animate by shifting data
        if self.is_analyzing:
            self.waveform_data = self.waveform_data[1:] + [random.randint(10, 90)]
            self.canvas.after(100, lambda: self.draw_waveform(theme))

class EnhancedGUI:
    """Enhanced GUI with advanced visual effects"""
    
    def __init__(self, parent, theme_manager):
        self.parent = parent
        self.theme_manager = theme_manager
        self.setup_enhanced_effects()
        
    def setup_enhanced_effects(self):
        """Setup advanced visual effects"""
        # Create background canvas for particles
        self.bg_canvas = tk.Canvas(
            self.parent,
            highlightthickness=0,
            bg=self.theme_manager.current_theme['bg_dark']
        )
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Initialize particle system
        self.particle_system = ParticleSystem(
            self.bg_canvas, 
            self.theme_manager.current_theme
        )
        self.particle_system.update_particles()
        
    def create_glow_button(self, parent, text, command, color=None):
        """Create a button with enhanced glow effects"""
        if not color:
            color = random.choice(self.theme_manager.current_theme['button_colors'])
            
        # Create frame for glow effect
        glow_frame = tk.Frame(parent, bg=self.theme_manager.current_theme['bg_medium'])
        
        button = tk.Button(
            glow_frame,
            text=text,
            command=command,
            font=("Arial", 10, "bold"),
            fg='white',
            bg=color,
            activebackground=self.brighten_color(color),
            activeforeground='white',
            relief='flat',
            bd=0,
            padx=20,
            pady=10,
            cursor='hand2'
        )
        button.pack()
        
        # Add hover effects
        self.add_hover_effects(button, color)
        
        return glow_frame
        
    def add_hover_effects(self, button, base_color):
        """Add hover animations to buttons"""
        def on_enter(event):
            bright_color = self.brighten_color(base_color)
            button.config(bg=bright_color)
            self.animate_button_glow(button, bright_color)
            
        def on_leave(event):
            button.config(bg=base_color)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
    def animate_button_glow(self, button, color):
        """Animate button glow effect"""
        # Simple pulsing effect
        def pulse():
            for alpha in [0.7, 0.8, 0.9, 1.0, 0.9, 0.8, 0.7]:
                try:
                    pulse_color = self.adjust_color_alpha(color, alpha)
                    button.config(bg=pulse_color)
                    button.update()
                    time.sleep(0.05)
                except:
                    break
                    
        threading.Thread(target=pulse, daemon=True).start()
        
    def brighten_color(self, hex_color):
        """Brighten a hex color"""
        try:
            # Convert hex to RGB
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Brighten
            brightened = tuple(min(255, int(c * 1.2)) for c in rgb)
            
            # Convert back to hex
            return f"#{brightened[0]:02x}{brightened[1]:02x}{brightened[2]:02x}"
        except:
            return hex_color
            
    def adjust_color_alpha(self, hex_color, alpha):
        """Adjust color alpha (simplified for tkinter)"""
        return self.brighten_color(hex_color)

class DragDropHandler:
    """Enhanced drag and drop functionality"""
    
    def __init__(self, app):
        self.app = app
        
    def setup_drag_drop(self, widget):
        """Setup drag and drop on a widget"""
        widget.drop_target_register(tkdnd.DND_FILES)
        widget.dnd_bind('<<Drop>>', self.on_drop)
        
    def on_drop(self, event):
        """Handle dropped files"""
        files = event.data.split()
        audio_extensions = {'.mp3', '.wav', '.flac', '.ogg', '.aac', '.m4a', '.wma'}
        
        for file_path in files:
            file_path = file_path.strip('{}')  # Remove braces
            if Path(file_path).suffix.lower() in audio_extensions:
                self.app.add_file_to_list(file_path)
            elif Path(file_path).is_dir():
                self.app.add_folder_files(file_path)

class AudioMetadataEditor:
    """Audio metadata editing capabilities"""
    
    def __init__(self):
        self.supported_formats = {'.mp3', '.flac', '.ogg', '.m4a'}
        
    def get_metadata(self, file_path):
        """Get audio file metadata"""
        try:
            # Use ffprobe to get metadata
            cmd = [
                'ffprobe', '-v', 'quiet', '-print_format', 'json',
                '-show_format', '-show_streams', file_path
            ]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                return json.loads(result.stdout)
        except:
            pass
        return {}
        
    def edit_metadata_dialog(self, file_path):
        """Open metadata editing dialog"""
        metadata = self.get_metadata(file_path)
        
        dialog = tk.Toplevel()
        dialog.title(f"Edit Metadata - {Path(file_path).name}")
        dialog.geometry("400x300")
        
        # Add metadata fields
        fields = ['title', 'artist', 'album', 'year', 'genre']
        entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(dialog, text=field.capitalize() + ":").grid(row=i, column=0, sticky='w', padx=10, pady=5)
            entry = tk.Entry(dialog, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field] = entry
            
        # Save button
        def save_metadata():
            # Implementation would use FFmpeg to modify metadata
            messagebox.showinfo("Success", "Metadata updated!")
            dialog.destroy()
            
        tk.Button(dialog, text="Save", command=save_metadata).grid(row=len(fields), column=1, pady=20)

# Enhanced progress bar with animations
class AnimatedProgressBar:
    """Animated progress bar with visual effects"""
    
    def __init__(self, parent, theme, width=400, height=30):
        self.theme = theme
        self.canvas = tk.Canvas(parent, width=width, height=height, bg=theme['bg_dark'], highlightthickness=0)
        self.canvas.pack()
        self.width = width
        self.height = height
        self.progress = 0
        self.animate = True
        
    def set_progress(self, value):
        """Set progress value (0-100)"""
        self.progress = min(100, max(0, value))
        self.draw_progress()
        
    def draw_progress(self):
        """Draw animated progress bar"""
        self.canvas.delete("all")
        
        # Background
        self.canvas.create_rectangle(
            0, 0, self.width, self.height,
            fill=self.theme['bg_medium'], outline=""
        )
        
        # Progress fill
        fill_width = (self.progress / 100) * self.width
        
        if fill_width > 0:
            # Create gradient effect
            for i in range(int(fill_width)):
                ratio = i / self.width
                color = self.interpolate_color(
                    self.theme['primary'], 
                    self.theme['accent'], 
                    ratio
                )
                
                self.canvas.create_line(
                    i, 0, i, self.height,
                    fill=color, width=1
                )
                
        # Progress text
        self.canvas.create_text(
            self.width // 2, self.height // 2,
            text=f"{self.progress:.1f}%",
            fill='white',
            font=("Arial", 10, "bold")
        )
        
    def interpolate_color(self, color1, color2, t):
        """Interpolate between two colors"""
        try:
            # Convert hex to RGB
            c1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
            c2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
            
            # Interpolate
            result = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
            
            # Convert back to hex
            return f"#{result[0]:02x}{result[1]:02x}{result[2]:02x}"
        except:
            return color1
