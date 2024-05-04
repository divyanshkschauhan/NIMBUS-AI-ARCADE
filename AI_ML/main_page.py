import tkinter as tk
from PIL import Image, ImageTk
import subprocess

def run_file1():
    subprocess.Popen(["python", r"sweeper_try.py"])

def run_file2():
    subprocess.Popen(["python", r"number_maze.py"])

def run_file3():
    subprocess.Popen(["python", "chess_main.py"])

def run_file4():
    subprocess.Popen(["python", "taxi.py"])

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def exit_app(event=None):
    root.destroy()


root = tk.Tk()
root.title("AI ARCADE")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


background_image = Image.open(r"Images\backg.jpg")
background_image = background_image.resize((screen_width, screen_height))
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Heading label with style
heading_label = tk.Label(root, text="AI ARCADE", font=("Arial", 36, "bold"), fg="white", bg="black")
heading_label.pack(side=tk.TOP, pady=40)

button_image1 = Image.open(r"Images\mine_img.png")  
button_image1 = button_image1.resize((286, 286))
button_photo1 = ImageTk.PhotoImage(button_image1)

button_image2 = Image.open(r"Images\num_img.png") 
button_image2 = button_image2.resize((286, 286))
button_photo2 = ImageTk.PhotoImage(button_image2)

button_image3 = Image.open(r"Images/chess_img.png")  
button_image3 = button_image3.resize((286, 286))
button_photo3 = ImageTk.PhotoImage(button_image3)

button_image4 = Image.open(r"Images/taxi_img.png")  
button_image4 = button_image4.resize((286, 286))
button_photo4 = ImageTk.PhotoImage(button_image4)


button1 = tk.Button(root, image=button_photo1, command=run_file1)
button1.image = button_photo1 
button1.pack(side=tk.LEFT, padx=10, pady=10)

button2 = tk.Button(root, image=button_photo2, command=run_file2)
button2.image = button_photo2 
button2.pack(side=tk.LEFT, padx=15, pady=15)

button3 = tk.Button(root, image=button_photo3, command=run_file3)
button3.image = button_photo3  
button3.pack(side=tk.LEFT, padx=20, pady=20)

button4 = tk.Button(root, image=button_photo4, command=run_file4)
button4.image = button_photo4  
button4.pack(side=tk.LEFT, padx=25, pady=25)


message_label = tk.Label(root, text="Press 'q' to exit", font=("Arial", 18), fg="white", bg="black")
message_label.pack(side=tk.BOTTOM, pady=0)

root.bind("<KeyPress-q>", toggle_fullscreen)

root.bind("<KeyPress-Q>", exit_app)

root.attributes('-fullscreen', True)

root.mainloop()
