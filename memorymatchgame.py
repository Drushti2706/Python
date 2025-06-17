import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match Game")
        self.buttons = []
        self.first = None
        self.second = None
        self.moves = 0

        # Prepare card values (8 pairs = 16 cards)
        self.values = list(range(1, 9)) * 2
        random.shuffle(self.values)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.status = tk.Label(self.root, text="Moves: 0", font=("Arial", 12))
        self.status.pack()

        self.create_buttons()
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

    def create_buttons(self):
        for i in range(4):
            row = []
            for j in range(4):
                btn = tk.Button(self.frame, text=" ", width=8, height=4,
                                command=lambda i=i, j=j: self.reveal_card(i, j))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def reveal_card(self, i, j):
        if self.buttons[i][j]['state'] == 'disabled':
            return

        index = i * 4 + j
        self.buttons[i][j]['text'] = str(self.values[index])
        self.buttons[i][j].update()

        if not self.first:
            self.first = (i, j)
        elif not self.second and (i, j) != self.first:
            self.second = (i, j)
            self.root.after(500, self.check_match)

    def check_match(self):
        i1, j1 = self.first
        i2, j2 = self.second
        v1 = self.values[i1 * 4 + j1]
        v2 = self.values[i2 * 4 + j2]

        if v1 == v2:
            self.buttons[i1][j1]['state'] = 'disabled'
            self.buttons[i2][j2]['state'] = 'disabled'
        else:
            self.buttons[i1][j1]['text'] = " "
            self.buttons[i2][j2]['text'] = " "

        self.moves += 1
        self.status.config(text=f"Moves: {self.moves}")
        self.first = None
        self.second = None

    def restart_game(self):
        self.values = list(range(1, 9)) * 2
        random.shuffle(self.values)
        self.moves = 0
        self.status.config(text="Moves: 0")
        self.first = None
        self.second = None
        for i in range(4):
            for j in range(4):
                btn = self.buttons[i][j]
                btn['text'] = " "
                btn['state'] = 'normal'

# Run the game
root = tk.Tk()
game = MemoryGame(root)
root.mainloop()
