import customtkinter as ctk
import subprocess
import sys
import os

# Set appearance
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Other options: "green", "dark-blue"

# Create App Window
app = ctk.CTk()
app.geometry("500x300")
app.title("Sign Language Translator")

# Title Label
title = ctk.CTkLabel(app, text="Sign Language Translator", font=ctk.CTkFont(size=20, weight="bold"))
title.pack(pady=20)

# Launch Button
def launch_translator():
    subprocess.Popen([sys.executable, "inference.py"], cwd=os.getcwd()) # Replace with your actual script

start_button = ctk.CTkButton(app, text="Start Translator", command=launch_translator)
start_button.pack(pady=10)

# Exit Button
exit_button = ctk.CTkButton(app, text="Exit", command=app.destroy)
exit_button.pack(pady=10)

# Run App
app.mainloop()
