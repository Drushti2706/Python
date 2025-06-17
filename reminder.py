# import pyttsx3
import tkinter as tk
from tkinter import messagebox
import pyttsx3
import threading
import time

# Voice engine
engine = pyttsx3.init()

# Store active countdown labels
active_labels = []

# Reminder thread
def wait_and_remind(message, seconds, label):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        label.config(text=f"Time left: {int(mins)}m {int(secs)}s")
        time.sleep(1)
        seconds -= 1
    label.config(text="Reminder Triggered!")
    messagebox.showinfo("Reminder", f"⏰ Reminder: {message}")
    engine.say(f"Reminder: {message}")
    engine.runAndWait()

# On button click
def set_reminder():
    msg = reminder_entry.get().strip()
    try:
        mins = float(time_entry.get())
        seconds = int(mins * 60)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter time in minutes (e.g., 0.1, 5, 10)")
        return

    if not msg:
        messagebox.showwarning("Missing Message", "Enter a reminder message.")
        return

    # Create a display label for countdown
    countdown_label = tk.Label(root, text="", font=("Arial", 10), fg="blue")
    countdown_label.pack()
    active_labels.append(countdown_label)

    messagebox.showinfo("Reminder Set", f"✅ Reminder set for {mins} minute(s).")

    # Start countdown in background
    threading.Thread(target=wait_and_remind, args=(msg, seconds, countdown_label)).start()

# GUI setup
root = tk.Tk()
root.title("Reminder App (Multi + Voice + Countdown)")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="📝 Reminder Message:", font=("Arial", 12)).pack(pady=10)
reminder_entry = tk.Entry(root, width=40, font=("Arial", 11))
reminder_entry.pack()

tk.Label(root, text="⏱️ Time (in minutes):", font=("Arial", 12)).pack(pady=10)
time_entry = tk.Entry(root, width=20, font=("Arial", 11))
time_entry.pack()

tk.Button(root, text="Set Reminder", command=set_reminder, font=("Arial", 12), bg="#007bff", fg="white").pack(pady=20)

tk.Label(root, text="📋 Active Reminders:", font=("Arial", 12, "bold")).pack(pady=10)

# Run the app
root.mainloop()
