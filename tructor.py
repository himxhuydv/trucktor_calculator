import tkinter as tk
from tkinter import messagebox

def convert_to_inches(value):
    """Convert hometown-style number (e.g. 12.5 = 12 ft 5 in) into inches."""
    if "." in value:
        feet, inch = value.split(".")
        return int(feet) * 12 + int(inch)
    else:
        return int(value) * 12

def calculate():
    try:
        h = height_entry.get()
        w = width_entry.get()
        b = breadth_entry.get()

        h_in = convert_to_inches(h)
        w_in = convert_to_inches(w)
        b_in = convert_to_inches(b)

        cu_in = h_in * w_in * b_in
        cu_ft = cu_in / 1728   # 1728 cubic inches in a cubic foot

        # Show result in a popup message
        messagebox.showinfo("Result", f"आयतन (Volume) = {cu_ft:.2f} cubic feet")

    except Exception:
        messagebox.showerror("Error", "कृपया सही संख्या डालें (Please enter valid numbers)")

# GUI setup
root = tk.Tk()
root.title("Truck Volume Calculator (ट्रक आयतन कैलकुलेटर)")
root.geometry("350x220")

tk.Label(root, text="Height ऊँचाई (जैसे 12.5 = 12ft 5in):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Label(root, text="Width चौड़ाई (जैसे 4.5 = 4ft 5in):").pack(pady=5)
width_entry = tk.Entry(root)
width_entry.pack()

tk.Label(root, text="breadth use it as example 255 ft.pack(pady=5)
breadth_entry = tk.Entry(root)
breadth_entry.pack()

tk.Button(root, text="Calculate हिसाब लगाएँ", command=calculate).pack(pady=10)

root.mainloop()
