import tkinter as tk

class FullscreenCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator - Fullscreen")
        self.expression = ""
        self.history = []

        self.root.attributes('-fullscreen', True)  # Fullscreen on launch
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))  # Exit fullscreen with Esc

        self.create_widgets()
        self.bind_keys()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=("Helvetica", 30), bd=10, relief="sunken", justify="right")
        self.display.pack(fill="x", padx=10, pady=10, ipady=15)

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both")

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', 'HIST']
        ]

        for r, row in enumerate(buttons):
            row_frame = tk.Frame(button_frame)
            row_frame.pack(expand=True, fill="both")
            for c, char in enumerate(row):
                btn = tk.Button(row_frame, text=char, font=("Helvetica", 24),
                                command=lambda x=char: self.on_click(x))
                btn.pack(side="left", expand=True, fill="both")

    def bind_keys(self):
        self.root.bind("<Key>", self.key_input)

    def key_input(self, event):
        key = event.char
        if key in '0123456789.+-*/':
            self.expression += key
            self.update_display()
        elif key == '\r':
            self.calculate()
        elif key.lower() == 'c':
            self.clear()

    def on_click(self, char):
        if char == '=':
            self.calculate()
        elif char == 'C':
            self.clear()
        elif char == 'HIST':
            self.show_history()
        else:
            self.expression += str(char)
            self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.history.append(f"{self.expression} = {result}")
            self.expression = result
            self.update_display()
        except:
            self.expression = ""
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def clear(self):
        self.expression = ""
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def show_history(self):
        hist_win = tk.Toplevel(self.root)
        hist_win.title("History")
        hist_win.geometry("300x200")
        tk.Label(hist_win, text="Calculation History", font=("Helvetica", 14, "bold")).pack(pady=10)
        for item in self.history[-10:]:
            tk.Label(hist_win, text=item, font=("Helvetica", 12)).pack(anchor="w", padx=10)

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = FullscreenCalculator(root)
    root.mainloop()
