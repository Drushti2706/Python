import tkinter as tk
from tkinter import messagebox

# Sample element database (can be expanded)
elements = {
    1: {"symbol": "H",  "name": "Hydrogen",  "mass": 1.008,  "group": 1, "period": 1},
    2: {"symbol": "He", "name": "Helium",    "mass": 4.0026, "group": 18, "period": 1},
    3: {"symbol": "Li", "name": "Lithium",   "mass": 6.94,   "group": 1, "period": 2},
    6: {"symbol": "C",  "name": "Carbon",    "mass": 12.011, "group": 14, "period": 2},
    7: {"symbol": "N",  "name": "Nitrogen",  "mass": 14.007, "group": 15, "period": 2},
    8: {"symbol": "O",  "name": "Oxygen",    "mass": 15.999, "group": 16, "period": 2},
    10: {"symbol": "Ne", "name": "Neon",     "mass": 20.18,  "group": 18, "period": 2},
    11: {"symbol": "Na", "name": "Sodium",   "mass": 22.99,  "group": 1, "period": 3},
    17: {"symbol": "Cl", "name": "Chlorine", "mass": 35.45,  "group": 17, "period": 3},
    26: {"symbol": "Fe", "name": "Iron",     "mass": 55.845, "group": 8, "period": 4},
    79: {"symbol": "Au", "name": "Gold",     "mass": 196.97, "group": 11, "period": 6},
    82: {"symbol": "Pb", "name": "Lead",     "mass": 207.2,  "group": 14, "period": 6},
}

# Reverse lookup by symbol and name
symbol_lookup = {v["symbol"].lower(): k for k, v in elements.items()}
name_lookup = {v["name"].lower(): k for k, v in elements.items()}

# === App ===
def find_element():
    query = entry.get().strip().lower()

    atomic_number = None

    if query.isdigit():
        atomic_number = int(query)
    elif query in symbol_lookup:
        atomic_number = symbol_lookup[query]
    elif query in name_lookup:
        atomic_number = name_lookup[query]

    if atomic_number and atomic_number in elements:
        data = elements[atomic_number]
        result_text.set(
            f"Element: {data['name']}\n"
            f"Symbol: {data['symbol']}\n"
            f"Atomic Number: {atomic_number}\n"
            f"Atomic Mass: {data['mass']}\n"
            f"Group: {data['group']}\n"
            f"Period: {data['period']}"
        )
    else:
        result_text.set("Element not found.")

# === GUI ===
root = tk.Tk()
root.title("Chemistry Element Finder")
root.geometry("400x300")

tk.Label(root, text="Enter Symbol, Name, or Atomic Number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack()

tk.Button(root, text="Search", font=("Arial", 12), command=find_element).pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
