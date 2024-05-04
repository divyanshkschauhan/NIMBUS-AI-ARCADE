import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def run_file1():
    subprocess.Popen(["python", r"C:\Users\divya\OneDrive\Pictures\Desktop\DLD LAB\sweeper_try.py"])

def run_file2():
    subprocess.Popen(["python", r"C:\Users\divya\AppData\Local\Programs\Python\Python311\aaaaaaa.py"])

def run_file3():
    subprocess.Popen(["python", "file3.py"])

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def exit_app(event=None):
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("AI ARCADE")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load the background image
background_image = Image.open(r"C:\AppData\AI_ML\Images\backg.jpg")
background_image = background_image.resize((screen_width, screen_height))
background_photo = ImageTk.PhotoImage(background_image)

# Create a label with the background image
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Load button images
button_image1 = Image.open(r"C:\AppData\AI_ML\Images\fourth.png")  # Replace "button_image1.png" with your image path
button_image1 = button_image1.resize((400, 400))
button_photo1 = ImageTk.PhotoImage(button_image1)

button_image2 = Image.open(r"C:\AppData\AI_ML\Images\third.png")  # Replace "button_image2.png" with your image path
button_image2 = button_image2.resize((400, 400))
button_photo2 = ImageTk.PhotoImage(button_image2)

button_image3 = Image.open(r"C:/AppData/AI_ML/Images/first.png")  # Replace "button_image3.png" with your image path
button_image3 = button_image3.resize((400, 400))
button_photo3 = ImageTk.PhotoImage(button_image3)

# Create buttons vertically aligned on the left side with images
button1 = tk.Button(root, image=button_photo1, command=run_file1)
button1.image = button_photo1  # Keep a reference to avoid garbage collection
button1.pack(side=tk.LEFT, padx=10, pady=10)

button2 = tk.Button(root, image=button_photo2, command=run_file2)
button2.image = button_photo2  # Keep a reference to avoid garbage collection
button2.pack(side=tk.LEFT, padx=15, pady=15)

button3 = tk.Button(root, image=button_photo3, command=run_file3)
button3.image = button_photo3  # Keep a reference to avoid garbage collection
button3.pack(side=tk.LEFT, padx=20, pady=20)

# Bind 'q' to toggle fullscreen
root.bind("<KeyPress-q>", toggle_fullscreen)

# Bind 'Q' to exit
root.bind("<KeyPress-Q>", exit_app)

# Initially open in fullscreen
root.attributes('-fullscreen', True)

# Message label
message_label = tk.Label(root, text="Press q to exit", font=("Arial", 12))
message_label.pack(side="bottom", pady=10)

# Run the Tkinter event loop
root.mainloop()
