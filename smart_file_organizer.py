import tkinter as tk
from tkinter import filedialog
import os
import shutil


def select_folder():

    folder = filedialog.askdirectory()

    if folder:
        folder_label.config(text=folder)


def organize_files():

    folder = folder_label.cget("text")

    if folder == "No folder selected":
        return

    count = 0

    for file in os.listdir(folder):

        
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()

            if extension in [".jpg", ".jpeg", ".png"]:
                category = "Images"

            elif extension in [".pdf", ".docx", ".txt"]:
                category = "Documents"

            elif extension in [".mp4", ".mkv", ".avi"]:
                category = "Videos"

            else:
                category = "Others"

            category_folder = os.path.join(folder, category)

            os.makedirs(category_folder, exist_ok=True)

            

            shutil.move(
            file_path,
            os.path.join(category_folder, file)
            )
            count += 1

    folder_label.config(
    text=f"✅ {count} files organized successfully!"
)


root = tk.Tk()

root.title("Smart File Organizer")

root.geometry("700x500")

root.configure(bg="#0f0f0f")


title_label = tk.Label(
    root,
    text="📁 Smart File Organizer",
    font=("Arial", 22, "bold"),
    bg="#0f0f0f",
    fg="#00ffcc"
)

title_label.pack(pady=20)


select_button = tk.Button(
    root,
    text="Select Folder",
    font=("Arial", 12),
    command=select_folder,
    bg="#0066ff",
    fg="white"
)

select_button.pack(pady=10)


organize_button = tk.Button(
    root,
    text="Organize Files",
    font=("Arial", 12),
    command=organize_files,
    bg="#00cc66",
    fg="white"
)

organize_button.pack(pady=10)


folder_label = tk.Label(
    root,
    text="No folder selected",
    wraplength=500,
    font=("Arial", 10),
    bg="#0f0f0f",
    fg="white"
)

folder_label.pack(pady=20)


root.mainloop()