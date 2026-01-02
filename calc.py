import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(False, False)

# Entry box
entry = tk.Entry(
    root,
    font=("Segoe UI", 20),
    bg="black",
    fg="white",
    bd=0,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipadx=10, ipady=10)

# Button functions
def press(v):
    entry.insert(tk.END, v)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons layout
buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

row = 1
col = 0

for b in buttons:
    if b == "=":
        btn = tk.Button(root, text=b, width=8, height=2, bg="orange",
                        fg="black", font=("Segoe UI", 14),
                        command=calculate)
    else:
        btn = tk.Button(root, text=b, width=8, height=2, bg="gray",
                        fg="white", font=("Segoe UI", 14),
                        command=lambda x=b: press(x))

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_btn = tk.Button(root, text="C", width=34, height=2,
                      bg="red", fg="white", font=("Segoe UI", 14),
                      command=clear)
clear_btn.grid(row=row, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
