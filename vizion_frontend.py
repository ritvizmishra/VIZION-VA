import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import vizion_backend  # Ensure start_listening() is defined there

def start_assistant():
    threading.Thread(target=vizion_backend.start_listening, daemon=True).start()

# Create main window
root = tk.Tk()
root.title("👁️ Vizion Assistant")
root.geometry("800x600")
root.configure(bg="#121212")
root.minsize(600, 400)

# Make it fullscreen and resizable
root.attributes("-fullscreen", True)

# Create a main frame to hold all widgets (for centering)
main_frame = tk.Frame(root, bg="#121212")
main_frame.pack(expand=True)

# Load and display a logo (optional, place 'vizion_logo.png' in same folder)
try:
    image = Image.open("vizion_logo.png")
    image = image.resize((150, 150), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(image)
    logo_label = tk.Label(main_frame, image=logo, bg="#121212")
    logo_label.pack(pady=(30, 10))
except:
    pass

# Title
title = tk.Label(main_frame, text="VIZION ASSISTANT", font=("Helvetica", 24, "bold"), fg="#4C74CB", bg="#121212")
title.pack(pady=(10, 40))

# Buttons
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),
                padding=10,
                foreground="#121212",
                background="#00FFB3")

start_button = ttk.Button(main_frame, text="🎙️ Start Listening", command=start_assistant)
start_button.pack(pady=10)

exit_button = ttk.Button(main_frame, text="❌ Exit", command=root.quit)
exit_button.pack(pady=10)

# Bind ESC key to exit full-screen
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# Start the GUI
root.mainloop()
