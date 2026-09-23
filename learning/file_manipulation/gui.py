import file_organizer as organizer
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

def on_button_click():
    selected_directory = filedialog.askdirectory()
    print(selected_directory)

label = tk.Label(root, text="Select a directory to organize:")
label.pack(pady=10)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()