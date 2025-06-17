import tkinter as tk
from tkinter import filedialog, messagebox, font

# === Functions ===
def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"{file_path} - Notepad")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        text_area.config(bg="#2E2E2E", fg="#FFFFFF", insertbackground='white')
    else:
        text_area.config(bg="white", fg="black", insertbackground='black')

def change_font_size(size):
    text_area.config(font=("Arial", size))

def exit_app():
    if messagebox.askyesno("Quit", "Exit the application?"):
        root.destroy()

def update_word_count(event=None):
    text = text_area.get(1.0, tk.END)
    words = len(text.split())
    chars = len(text) - 1
    word_count_label.config(text=f"Words: {words} | Chars: {chars}")

# === GUI Setup ===
root = tk.Tk()
root.title("Enhanced Notepad")
root.geometry("700x500")

text_area = tk.Text(root, font=("Arial", 12), undo=True, wrap="word")
text_area.pack(expand=True, fill='both')

# === Menu ===
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
view_menu = tk.Menu(menu_bar, tearoff=0)
font_menu = tk.Menu(menu_bar, tearoff=0)

# File Menu
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")
menu_bar.add_cascade(label="File", menu=file_menu)

# View Menu
view_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)
menu_bar.add_cascade(label="View", menu=view_menu)

# Font Size Menu
for size in [10, 12, 14, 16, 18, 20]:
    font_menu.add_command(label=f"{size}px", command=lambda s=size: change_font_size(s))
menu_bar.add_cascade(label="Font Size", menu=font_menu)

root.config(menu=menu_bar)

# === Status Bar ===
word_count_label = tk.Label(root, text="Words: 0 | Chars: 0", anchor='e')
word_count_label.pack(fill=tk.X, side=tk.BOTTOM)

# === Bindings ===
text_area.bind("<KeyRelease>", update_word_count)
root.bind("<Control-s>", save_file)
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-q>", lambda event: exit_app())

# === State ===
dark_mode = False

# === Run ===
update_word_count()
root.mainloop()
