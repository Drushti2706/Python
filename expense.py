import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

FILE_NAME = "expenses.csv"

# Create file if it doesn't exist
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_NAME, index=False)

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.geometry("400x400")

        # Title
        tk.Label(root, text="Expense Tracker", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Entry Fields
        self.date_var = tk.StringVar()
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))

        self.category_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        self.build_form()

    def build_form(self):
        tk.Label(self.root, text="Date (YYYY-MM-DD):").pack(pady=5)
        tk.Entry(self.root, textvariable=self.date_var).pack()

        tk.Label(self.root, text="Category:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.category_var).pack()

        tk.Label(self.root, text="Amount:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.amount_var).pack()

        # Buttons
        tk.Button(self.root, text="Add Expense", command=self.add_expense).pack(pady=10)
        tk.Button(self.root, text="Show Summary", command=self.show_summary).pack(pady=5)
        tk.Button(self.root, text="Plot Expenses", command=self.plot_expenses).pack(pady=5)

    def add_expense(self):
        date = self.date_var.get()
        category = self.category_var.get()
        amount = self.amount_var.get()

        try:
            datetime.strptime(date, "%Y-%m-%d")  # Validate date format
            amount = float(amount)  # Validate amount
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid date and amount.")
            return

        # Append to CSV
        new_entry = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
        new_entry.to_csv(FILE_NAME, mode='a', header=False, index=False)

        messagebox.showinfo("Success", "Expense added successfully!")

        self.category_var.set("")
        self.amount_var.set("")

    def show_summary(self):
        df = pd.read_csv(FILE_NAME)
        if df.empty:
            messagebox.showinfo("No Data", "No expenses found.")
            return

        total = df["Amount"].sum()
        summary = df.groupby("Category")["Amount"].sum()
        summary_text = f"Total: ₹{total:.2f}\n\nBreakdown:\n"

        for cat, amt in summary.items():
            summary_text += f"{cat}: ₹{amt:.2f}\n"

        messagebox.showinfo("Expense Summary", summary_text)

    def plot_expenses(self):
        df = pd.read_csv(FILE_NAME)
        if df.empty:
            messagebox.showinfo("No Data", "No expenses to plot.")
            return

        summary = df.groupby("Category")["Amount"].sum()
        summary.plot(kind="bar", title="Expenses by Category")
        plt.ylabel("Amount (₹)")
        plt.tight_layout()
        plt.show()

# Launch app
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
