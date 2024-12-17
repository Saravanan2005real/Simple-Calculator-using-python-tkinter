import tkinter as tk

# Function to handle button click
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.set(result)
        except Exception:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x640")
root.resizable(False, False)

# Brand name label
brand_label = tk.Label(
    root, text="Casio", font=("Arial", 20, "bold"), fg="#2d3436", bg="#ffffff"
)
brand_label.pack(fill=tk.BOTH, pady=10)

# StringVar to store the input
entry = tk.StringVar()

# Entry field
entry_field = tk.Entry(
    root, textvar=entry, font=("Arial", 24), bd=10, relief=tk.FLAT, justify=tk.RIGHT
)
entry_field.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=15)

# Button frame
button_frame = tk.Frame(root, bg="#f1f2f6")
button_frame.pack(pady=10)

# Button layout
buttons = [
    "C", "", "", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "=", "%",
]

# Style variables
btn_bg = "#f1f2f6"
btn_fg = "#2d3436"
operator_bg = "#fab1a0"
operator_fg = "#ffffff"

# Create and place buttons
row_val = 0
col_val = 0

for button_text in buttons:
    if button_text != "":
        btn_color = operator_bg if button_text in "/*-+=%" else btn_bg
        text_color = operator_fg if button_text in "/*-+=%" else btn_fg

        button = tk.Button(
            button_frame,
            text=button_text,
            font=("Arial", 18, "bold"),
            bg=btn_color,
            fg=text_color,
            relief=tk.RAISED,
            bd=3,
            width=4,
            height=2,
        )
        button.grid(row=row_val, column=col_val, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter main loop
root.mainloop()
