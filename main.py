import tkinter as tk
from tkinter import filedialog

# create main window
window = tk.Tk()
window.title("Let's Build a Text Editor")
window.geometry("700x500")

# create text area
text_area = tk.Text(window, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# ---------------- FUNCTIONS ----------------

# clear text
def clear_text():
    text_area.delete(1.0, tk.END)

# open file
def open_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        text_area.delete(1.0, tk.END)
        with open(file, "r") as f:
            text_area.insert(tk.END, f.read())

# save file
def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "w") as f:
            f.write(text_area.get(1.0, tk.END))

# ---------------- MENU BAR ----------------

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

# run program
window.mainloop()
