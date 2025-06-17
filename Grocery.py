import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime

# Initial Inventory
inventory = {
    "Rice": {"price": 50, "stock": 100},
    "Wheat": {"price": 40, "stock": 80},
    "Oil": {"price": 120, "stock": 50},
    "Sugar": {"price": 45, "stock": 60},
    "Salt": {"price": 20, "stock": 70}
}

cart = {}
GST_RATE = 0.05

# GUI Window
root = tk.Tk()
root.title("Grocery Store Management System")
root.geometry("600x500")

# UI Elements
cart_text = tk.Text(root, height=15, width=70)
cart_text.pack(pady=10)

def refresh_inventory():
    inventory_list.delete(0, tk.END)
    for item in inventory:
        details = inventory[item]
        inventory_list.insert(tk.END, f"{item} - Rs{details['price']} - {details['stock']}kg")

def add_to_cart():
    selected = inventory_list.curselection()
    if not selected:
        messagebox.showwarning("Select Item", "Please select an item.")
        return
    item_line = inventory_list.get(selected)
    item = item_line.split(" - ")[0]
    try:
        qty = int(qty_entry.get())
        if qty <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Quantity", "Enter a valid positive integer.")
        return

    if qty > inventory[item]['stock']:
        messagebox.showerror("Stock Error", "Not enough stock.")
        return

    inventory[item]['stock'] -= qty
    if item in cart:
        cart[item]['quantity'] += qty
    else:
        cart[item] = {"price": inventory[item]['price'], "quantity": qty}

    refresh_inventory()
    update_cart_display()
    qty_entry.delete(0, tk.END)

def update_cart_display():
    cart_text.delete(1.0, tk.END)
    total = 0
    for item, details in cart.items():
        item_total = details['price'] * details['quantity']
        cart_text.insert(tk.END, f"{item}: {details['quantity']}kg x Rs{details['price']} = Rs{item_total}\n")
        total += item_total
    gst = total * GST_RATE
    grand_total = total + gst
    cart_text.insert(tk.END, f"\nSubtotal: Rs{total}")
    cart_text.insert(tk.END, f"\nGST (5%): Rs{gst:.2f}")
    cart_text.insert(tk.END, f"\nTotal Amount: Rs{grand_total:.2f}")

def save_bill():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    filename = f"bill_{now}.txt"
    with open(filename, "w") as f:
        f.write(cart_text.get(1.0, tk.END))
    messagebox.showinfo("Saved", f"Bill saved as {filename}")

def admin_login():
    username = simpledialog.askstring("Admin Login", "Enter username:")
    password = simpledialog.askstring("Admin Login", "Enter password:", show="*")
    if username == "admin" and password == "1234":
        admin_panel()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")

def admin_panel():
    def add_item():
        name = simpledialog.askstring("New Item", "Enter item name:")
        price = simpledialog.askinteger("Price", "Enter price:")
        stock = simpledialog.askinteger("Stock", "Enter stock quantity:")
        if name and price and stock:
            inventory[name.title()] = {"price": price, "stock": stock}
            refresh_inventory()

    def update_price():
        name = simpledialog.askstring("Item Name", "Enter item to update:")
        if name in inventory:
            price = simpledialog.askinteger("New Price", "Enter new price:")
            if price:
                inventory[name]['price'] = price
                refresh_inventory()
        else:
            messagebox.showerror("Not Found", "Item not found.")

    def remove_item():
        name = simpledialog.askstring("Remove Item", "Enter item name to remove:")
        if name in inventory:
            del inventory[name]
            refresh_inventory()
        else:
            messagebox.showerror("Not Found", "Item not found.")

    admin_win = tk.Toplevel(root)
    admin_win.title("Admin Panel")
    admin_win.geometry("300x200")

    tk.Button(admin_win, text="Add Item", command=add_item).pack(pady=5)
    tk.Button(admin_win, text="Update Price", command=update_price).pack(pady=5)
    tk.Button(admin_win, text="Remove Item", command=remove_item).pack(pady=5)
    tk.Button(admin_win, text="Close", command=admin_win.destroy).pack(pady=5)

# Inventory Frame
frame = tk.Frame(root)
frame.pack()

inventory_list = tk.Listbox(frame, height=8, width=40)
inventory_list.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=inventory_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
inventory_list.config(yscrollcommand=scrollbar.set)

qty_entry = tk.Entry(root)
qty_entry.pack()
qty_entry.insert(0, "1")

tk.Button(root, text="Add to Cart", command=add_to_cart).pack(pady=5)
tk.Button(root, text="Save Bill", command=save_bill).pack(pady=5)
tk.Button(root, text="Admin Login", command=admin_login).pack(pady=5)

refresh_inventory()
root.mainloop()
