#pip install pyttsx3
import tkinter as tk
import random
import pyttsx3
from datetime import datetime

# Quote dictionary by mood
quotes = {
    "Happy": [
        "Keep smiling, life is beautiful!",
        "Happiness is a journey, not a destination.",
        "Your joy is contagious!"
    ],
    "Sad": [
        "Every storm runs out of rain.",
        "It's okay to feel down. You’re stronger than you think.",
        "Tough times never last, but tough people do."
    ],
    "Angry": [
        "Take a deep breath. Let it go.",
        "Don't let anger control you, control it.",
        "Speak when you’re calm, not when you’re angry."
    ],
    "Stressed": [
        "Breathe in calm, breathe out stress.",
        "This too shall pass.",
        "Relax. You’ve handled so much already, you’ll handle this too."
    ]
}

engine = pyttsx3.init()

def speak_quote(text):
    engine.say(text)
    engine.runAndWait()

def show_quote():
    mood = mood_var.get()
    if mood:
        quote = random.choice(quotes[mood])
        result_label.config(text=quote)
        if tts_var.get():
            speak_quote(quote)
    else:
        result_label.config(text="Please select a mood.")

def save_quote():
    mood = mood_var.get()
    quote = result_label.cget("text")
    if quote and mood:
        with open("quotes_log.txt", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mood}: {quote}\n")
        status_label.config(text="Quote saved to quotes_log.txt")
    else:
        status_label.config(text="No quote to save.")

def copy_quote():
    quote = result_label.cget("text")
    if quote:
        root.clipboard_clear()
        root.clipboard_append(quote)
        status_label.config(text="Quote copied to clipboard.")

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg = "#1e1e1e" if dark_mode else "#ffffff"
    fg = "#ffffff" if dark_mode else "#000000"
    button_color = "#444444" if dark_mode else "#4CAF50"
    
    root.config(bg=bg)
    for widget in root.winfo_children():
        widget.config(bg=bg, fg=fg)
        if isinstance(widget, tk.Button):
            widget.config(bg=button_color, activebackground="#666" if dark_mode else "#81C784")
        elif isinstance(widget, tk.Label):
            widget.config(bg=bg, fg=fg)

# === GUI ===
root = tk.Tk()
root.title("Mood-Based Quote Generator")
root.geometry("500x400")
dark_mode = False

mood_var = tk.StringVar()
tts_var = tk.BooleanVar()

tk.Label(root, text="How are you feeling?", font=("Arial", 14)).pack(pady=10)

# Mood radio buttons
for mood in quotes.keys():
    tk.Radiobutton(root, text=mood, variable=mood_var, value=mood, font=("Arial", 12)).pack(anchor="w", padx=20)

# TTS option
tk.Checkbutton(root, text="Speak the quote aloud", variable=tts_var, font=("Arial", 11)).pack(pady=5)

# Buttons
tk.Button(root, text="Get Quote", command=show_quote, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Save Quote", command=save_quote, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_quote, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Toggle Dark Mode", command=toggle_theme, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)

# Quote output
result_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12), justify="center", fg="blue")
result_label.pack(pady=10)

# Status message
status_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
status_label.pack()

root.mainloop()
