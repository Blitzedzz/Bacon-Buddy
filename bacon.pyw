import os
import sys

if os.path.basename(sys.executable).lower() == "py.exe":
    python_executable = "python.exe"
    command = f"{python_executable} {' '.join(sys.argv)}"
    os.system(command)
    sys.exit()

os.system('python.exe -m pip install --upgrade pip >nul')
os.system('pip install tk >nul')
os.system('pip install pillow >nul')
os.system('pip install pygame >nul')
os.system('pip install winshell >nul')

import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import sys
import platform

# made by blitzedzz
class DesktopBuddy:
    def __init__(self, root, image_path, sounds_folder):
        self.root = root
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.geometry("+300+300")  # Initial position
        self.root.attributes("-topmost", True)  # Make window topmost
        self.root.wm_attributes("-transparentcolor", 'white')  # Make white color transparent

        # Initialize pygame mixer
        pygame.mixer.init()

        # Load sound files
        self.sounds = [os.path.join(sounds_folder, file) for file in os.listdir(sounds_folder) if file.endswith(('.wav', '.mp3'))]

        # Load and resize the image
        self.image = Image.open(image_path)
        self.image = self.image.resize((150, 150), Image.LANCZOS)  # Resize image to 150x150 pixels
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(root, image=self.photo, bg='white')
        self.label.pack()

        self.label.bind("<Button-1>", self.on_click)
        self.label.bind("<Button-1>", self.start_move, add='+')
        self.label.bind("<ButtonRelease-1>", self.stop_move)
        self.label.bind("<B1-Motion>", self.on_move)
        self.label.bind("<Button-3>", self.on_right_click)  # Bind right-click to show menu

        # Create a menu for right-click
        self.menu = tk.Menu(root, tearoff=0)
        self.menu.add_command(label="Quit", command=self.root.destroy)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_move(self, event):
        x = (event.x_root - self.x)
        y = (event.y_root - self.y)
        self.root.geometry(f"+{x}+{y}")

    def on_click(self, event):
        if self.sounds:
            sound_file = random.choice(self.sounds)
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

    def on_right_click(self, event):
        self.menu.post(event.x_root, event.y_root)

def add_to_startup():
    
    if platform.system() == "Windows":
        startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
        script_path = os.path.abspath(sys.argv[0])
        startup_script = os.path.join(startup_folder, "DesktopBuddy.lnk")
        
        import winshell
        with winshell.shortcut(startup_script) as link:
            link.path = sys.executable
            link.arguments = script_path
            link.working_directory = os.path.dirname(script_path)
            link.description = "Desktop Buddy"


if __name__ == "__main__":
    add_to_startup()
    root = tk.Tk()
    app = DesktopBuddy(root, "bacon.png", "sounds")  # Replace with your bacon image path and sounds folder
    root.mainloop()
