import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry("400x400")

        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.total_rounds = 3  # Can be changed to 5 for Best of 5

        self.choices = ['Rock', 'Paper', 'Scissors']

        self.create_widgets()

    def create_widgets(self):
        self.label_title = tk.Label(self.root, text="Rock Paper Scissors", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=10)

        self.label_result = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.label_result.pack(pady=10)

        self.label_score = tk.Label(self.root, text="Your Score: 0 | Computer Score: 0", font=("Helvetica", 12))
        self.label_score.pack(pady=10)

        self.label_round = tk.Label(self.root, text="Round: 1 / " + str(self.total_rounds), font=("Helvetica", 12))
        self.label_round.pack(pady=10)

        # Buttons
        self.frame_buttons = tk.Frame(self.root)
        self.frame_buttons.pack(pady=10)

        for choice in self.choices:
            btn = tk.Button(self.frame_buttons, text=choice, width=10, command=lambda c=choice: self.play(c))
            btn.pack(side="left", padx=5)

        self.button_restart = tk.Button(self.root, text="Restart Game", command=self.reset_game, state="disabled")
        self.button_restart.pack(pady=20)

    def play(self, user_choice):
        if self.rounds_played >= self.total_rounds:
            return

        computer_choice = random.choice(self.choices)
        result = ""

        if user_choice == computer_choice:
            result = f"Both chose {user_choice}. It's a tie."
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Paper' and computer_choice == 'Rock') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper'):
            result = f"You chose {user_choice}, Computer chose {computer_choice}. You win this round!"
            self.user_score += 1
        else:
            result = f"You chose {user_choice}, Computer chose {computer_choice}. Computer wins this round!"
            self.computer_score += 1

        self.rounds_played += 1
        self.label_result.config(text=result)
        self.label_score.config(text=f"Your Score: {self.user_score} | Computer Score: {self.computer_score}")
        self.label_round.config(text=f"Round: {self.rounds_played + 1} / {self.total_rounds}")

        if self.rounds_played == self.total_rounds:
            final_result = ""
            if self.user_score > self.computer_score:
                final_result = "You win the game!"
            elif self.computer_score > self.user_score:
                final_result = "Computer wins the game!"
            else:
                final_result = "The game is a tie!"

            self.label_result.config(text=self.label_result.cget("text") + "\n" + final_result)
            self.button_restart.config(state="normal")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.label_result.config(text="")
        self.label_score.config(text="Your Score: 0 | Computer Score: 0")
        self.label_round.config(text="Round: 1 / " + str(self.total_rounds))
        self.button_restart.config(state="disabled")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
