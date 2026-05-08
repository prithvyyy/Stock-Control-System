import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

from product import Product
from file_handler import load_products, save_products

products = load_products()

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    for index, p in enumerate(products):
        tree.insert("", "end", iid=index, values=(p.model, p.name, p.quantity))


def clear_inputs():
    entry_model.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_update.delete(0, tk.END)


def add_product():
    model = entry_model.get().strip()
    name = entry_name.get().strip()
    qty = entry_quantity.get().strip()

    if not model or not name or not qty:
        messagebox.showerror("Error", "All fields are required")
        return

    if not model.isdigit():
        messagebox.showerror("Error", "Model must be numeric")
        return

    if not name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Name must contain only letters")
        return

    try:
        qty = int(qty)
        if qty < 0:
            raise ValueError

        for p in products:
            if p.model == model:
                messagebox.showerror("Error", "Model already exists")
                return

        products.append(Product(model, name, qty))
        save_products(products)
        refresh_table()
        clear_inputs()

    except:
        messagebox.showerror("Error", "Quantity must be a positive integer")


def remove_product():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a product first")
        return

    if not messagebox.askyesno("Confirm", "Delete this product?"):
        return

    index = int(selected[0])
    products.pop(index)

    save_products(products)
    refresh_table()


def update_stock():
    selected = tree.selection()

    if not selected:
        messagebox.showwarning("Warning", "Select a product")
        return

    change_text = entry_update.get().strip()

    if not change_text:
        messagebox.showerror("Error", "Enter a value")
        return

    try:
        change = int(change_text)
        index = int(selected[0])

        products[index].update_stock(change)

        save_products(products)
        refresh_table()
        entry_update.delete(0, tk.END)

        messagebox.showinfo("Success", "Stock updated")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_graph():
    if not products:
        messagebox.showwarning("Warning", "No data to display")
        return

    names = [p.name for p in products]
    quantities = [p.quantity for p in products]

    plt.figure()
    plt.bar(names, quantities)
    plt.xlabel("Products")
    plt.ylabel("Quantity")
    plt.title("Stock Levels")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()


root = tk.Tk()
root.title("Stock Control System")
root.geometry("500x500")

tk.Label(root, text="Model").pack()
entry_model = tk.Entry(root)
entry_model.pack()

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Quantity").pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

tk.Button(root, text="Add Product", command=add_product).pack(pady=5)

tree = ttk.Treeview(root, columns=("Model", "Name", "Quantity"), show="headings")
tree.heading("Model", text="Model")
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.pack(fill=tk.BOTH, expand=True)

tree.bind("<<TreeviewSelect>>", lambda e: entry_update.focus())

tk.Label(root, text="Update Stock (+/-)").pack()
entry_update = tk.Entry(root)
entry_update.pack()

tk.Button(root, text="Update Stock", command=update_stock).pack(pady=5)

tk.Button(root, text="Remove Product", command=remove_product).pack(pady=5)
tk.Button(root, text="Show Graph", command=show_graph).pack(pady=5)

refresh_table()
root.mainloop()