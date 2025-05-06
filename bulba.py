import tkinter as tk

root = tk.Tk()
root.geometry('400x260+100+300')
root.overrideredirect(True)

first_window = None
second_window = None
third_window = None
forth_window = None

def is_p(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_p(start):
    num = start + 1
    while not is_p(num):
        num += 1
    return num

def on_click():
    global click_count, current
    click_count += 1
    current = next_p(current)
    button.config(text=f"{click_count}: {current}")

def toggle_first_window():        # First window (Prime number button)
    global first_window
    if first_window is None or not first_window.winfo_exists():
        # Create first window
        first_window = tk.Toplevel(root)
        first_window.geometry('400x260+550+300')
        first_window.overrideredirect(True)
        button = tk.Button(first_window, text="0: 1", command=on_click, width="10", height="1", bg="grey", fg="white", font=("Arial", 30))
        button.place(anchor="center", x=200, y=50)
        btn_open_first.config(text="Close First Window")
    else:
        # Close first window
        first_window.destroy()
        first_window = None
        btn_open_first.config(text="Open First Window")

def toggle_second_window():        # Second window (Text and Entry)
    global second_window
    if second_window is None or not second_window.winfo_exists():
        second_window = tk.Toplevel(root)
        second_window.geometry('400x260+550+300')
        second_window.overrideredirect(True)
        t1 = tk.Text(second_window, height=3, width=25)  # Intrestin history start text
        t1.place(anchor="center", x=200, y=50)
        e1 = tk.Entry(second_window)  # Password input
        e1.place(anchor="center", x=200, y=100)
        t3 = tk.Text(second_window, height=3, width=25)  # Unexpected history end output when password is correct
        t3.place(anchor="center", x=200, y=150)
        btn_open_second.config(text="Close Second Window")
    else:
        # Close first window
        second_window.destroy()
        second_window = None
        btn_open_second.config(text="Open Second Window")

def toggle_third_window():        # Third window (Checkbuttons)
    def update_text():
        t2.delete(1.0, tk.END)
        active_letters = []
        if var_a.get():
            active_letters.append("A")
        if var_b.get():
            active_letters.append("B")
        if var_c.get():
            active_letters.append("C")
        if var_d.get():
            active_letters.append("D")
        if var_e.get():
            active_letters.append("E")
        t2.insert(tk.END, ''.join(active_letters))

    global third_window
    if third_window is None or not third_window.winfo_exists():
        third_window = tk.Toplevel(root)
        third_window.geometry('400x260+550+300')
        third_window.overrideredirect(True)
        t2 = tk.Text(third_window, height=2, width=25)
        t2.place(anchor="center", x=200, y=50)
        var_a = tk.IntVar()
        var_b = tk.IntVar()
        var_c = tk.IntVar()
        var_d = tk.IntVar()
        var_e = tk.IntVar()
        f1 = tk.Checkbutton(third_window, text="A", variable=var_a, command=update_text, width=2, height=2, bg="grey", fg="black")
        f1.place(anchor="center", x=112, y=150)
        f2 = tk.Checkbutton(third_window, text="B", variable=var_b, command=update_text, width=2, height=2, bg="grey", fg="black")
        f2.place(anchor="center", x=156, y=150)
        f3 = tk.Checkbutton(third_window, text="C", variable=var_c, command=update_text, width=2, height=2, bg="grey", fg="black")
        f3.place(anchor="center", x=200, y=150)
        f4 = tk.Checkbutton(third_window, text="D", variable=var_d, command=update_text, width=2, height=2, bg="grey", fg="black")
        f4.place(anchor="center", x=244, y=150)
        f5 = tk.Checkbutton(third_window, text="E", variable=var_e, command=update_text, width=2, height=2, bg="grey", fg="black")
        f5.place(anchor="center", x=288, y=150)
        btn_open_third.config(text="Close Third Window")
    else:
        third_window.destroy()
        third_window = None
        btn_open_third.config(text="Open Third Window")

def toggle_forth_window():
    global forth_window
    if forth_window is None or not forth_window.winfo_exists():
        forth_window = tk.Toplevel(root)
        forth_window.geometry('400x260+550+300')
        forth_window.overrideredirect(True)
        btn_open_forth.config(text="Close Froth Window")
    else:
        forth_window.destroy()
        forth_window = None
        btn_open_forth.config(text="Open Forth Window")

def close_root():
    root.destroy()


btn_open_first = tk.Button(root, text="Open First Window", command=toggle_first_window, width=20, height=2, bg="lightgoldenrodyellow")
btn_open_first.place(anchor="center", x=200, y=30)
btn_open_second = tk.Button(root, text="Open Second Window", command=toggle_second_window, width=20, height=2, bg="lightblue")
btn_open_second.place(anchor="center", x=200, y=80)
btn_open_third = tk.Button(root, text="Open Third Window", command=toggle_third_window, width=20, height=2, bg="lightcoral")
btn_open_third.place(anchor="center", x=200, y=130)
btn_open_forth = tk.Button(root, text="Open Forth Window", command=toggle_forth_window, width=20, height=2, bg="lightgreen")
btn_open_forth.place(anchor="center", x=200, y=180)
btn_root_destroy = tk.Button(root, text="Close", command=close_root, width=20, height=2, bg="grey")
btn_root_destroy.place(anchor="center", x=200, y=230)

root.tk.mainloop()
