import tkinter as tk
from tkinter import messagebox

def convert_weight():
    try:
        val = float(entry_weight.get())
        if var_opt.get() == "K":
            res = round(val * 2.20, 1)
            label_result.config(text=f"Result: {res} lbs")
        else:
            res = round(val / 2.20, 1)
            label_result.config(text=f"Result: {res} kg")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

root = tk.Tk()
root.title("Weight Converter")
root.geometry("250x200")

tk.Label(root, text="Enter Weight:").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

var_opt = tk.StringVar(value="K")
tk.Radiobutton(root, text="Kg to Lbs", variable=var_opt, value="K").pack()
tk.Radiobutton(root, text="Lbs to Kg", variable=var_opt, value="L").pack()

tk.Button(root, text="Convert", command=convert_weight).pack(pady=10)
label_result = tk.Label(root, text="Result: ", font=("Arial", 11, "bold"))
label_result.pack(pady=5)

root.mainloop()