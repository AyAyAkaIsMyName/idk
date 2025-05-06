import tkinter as tk

root = tk.Tk()
root.geometry('400x260+100+300')
root.overrideredirect(True)

first_window = None
second_window = None
third_window = None
forth_window = None

click_count = 0
current = 1

def toggle_first_window():        # First window (Prime number button)
    global first_window, click_count, current
    if first_window is None or not first_window.winfo_exists():

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

        click_count = 0
        current = 1
        first_window = tk.Toplevel(root)
        first_window.geometry('400x260+550+300')
        first_window.overrideredirect(True)
        button = tk.Button(first_window, text="0: 1", command=on_click, width="10", height="1", bg="lightgrey", fg="black", font=("Arial", 30))
        button.place(anchor="center", x=200, y=125)
        btn_open_first.config(text="Close First Window")
    else:
        first_window.destroy()
        first_window = None
        click_count = 0
        current = 1
        btn_open_first.config(text="Open First Window")

def toggle_second_window():        # Second window (Text and Entry)
    global second_window
    if second_window is None or not second_window.winfo_exists():
        second_window = tk.Toplevel(root)
        second_window.geometry('400x260+550+300')
        second_window.overrideredirect(True)
        t1 = tk.Text(second_window, height=5, width=30, bg="lightgray", fg="black", font=("Arial", 10))
        t1.place(anchor="center", x=200, y=50)
        t1.insert(tk.END, "В одном маленьком городке жил-был старый мудрец. Каждый день он сидел под большим деревом и рассказывал прохожим удивительные истории о далеких странах и приключениях. Люди собирались вокруг него, чтобы услышать его мудрость и вдохновение.")
        t1.config(state="disabled")
        l1 = tk.Label(second_window, text="Пароль:", font=("Arial", 14))
        l1.place(anchor="center", x=200, y=109)
        e1 = tk.Entry(second_window, show="*", bg="lightgray", fg="black")
        e1.place(anchor="center", x=200, y=130)
        t3 = tk.Text(second_window, height=5, width=30, bg="lightgray", fg="black", font=("Arial", 10))
        t3.place(anchor="center", x=200, y=200)
        t3.config(state="disabled")
        def check_password(event=None):
            pwd = e1.get()
            if pwd == "1234abcd":
                t3.config(state="normal")
                t3.delete("1.0", tk.END)
                t3.insert(tk.END, "Однажды к мудрецу подошел юноша и спросил: 'Как мне стать таким же мудрым, как ты?' Мудрец ответил: 'Чтобы обрести мудрость, нужно не только слушать, но и учиться на своих ошибках. И помни, что истинная мудрость приходит с опытом и терпением.' С тех пор юноша начал свой путь к знаниям, и его жизнь изменилась навсегда.")
                t3.config(state="disabled")
            else:
                t3.config(state="normal")
                t3.delete("1.0", tk.END)
                t3.config(state="disabled")
        e1.bind("<KeyRelease>", check_password)
        btn_open_second.config(text="Close Second Window")
    else:
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
        t2 = tk.Text(third_window, height=1, width=7, font=("Arial", 41), bg="lightgrey")
        t2.place(anchor="center", x=200, y=70)
        var_a = tk.IntVar()
        var_b = tk.IntVar()
        var_c = tk.IntVar()
        var_d = tk.IntVar()
        var_e = tk.IntVar()
        f1 = tk.Checkbutton(third_window, text="A", variable=var_a, command=update_text, width=2, height=2, bg="white", fg="black", font=("Arial", 15))
        f1.place(anchor="center", x=112, y=150)
        f2 = tk.Checkbutton(third_window, text="B", variable=var_b, command=update_text, width=2, height=2, bg="white", fg="black", font=("Arial", 15))
        f2.place(anchor="center", x=156, y=150)
        f3 = tk.Checkbutton(third_window, text="C", variable=var_c, command=update_text, width=2, height=2, bg="white", fg="black", font=("Arial", 15))
        f3.place(anchor="center", x=200, y=150)
        f4 = tk.Checkbutton(third_window, text="D", variable=var_d, command=update_text, width=2, height=2, bg="white", fg="black", font=("Arial", 15))
        f4.place(anchor="center", x=244, y=150)
        f5 = tk.Checkbutton(third_window, text="E", variable=var_e, command=update_text, width=1, height=2, bg="white", fg="black", font=("Arial", 15))
        f5.place(anchor="center", x=288, y=150)
        btn_open_third.config(text="Close Third Window")
    else:
        third_window.destroy()
        third_window = None
        btn_open_third.config(text="Open Third Window")

def toggle_forth_window():        # Forth window (Raadiobuttons)
    global forth_window
    if forth_window is None or not forth_window.winfo_exists():
        forth_window = tk.Toplevel(root)
        forth_window.overrideredirect(True)
        forth_window.geometry('400x260+550+300')
        label = tk.Label(forth_window, text="Выбери последовательность:", font=("Arial", 14))
        label.pack(pady=5)
        var_seq = tk.StringVar(value="Фибоначи")
        label2 = tk.Label(forth_window, text="Кол-во чисел:", font=("Arial", 14))
        label2.place(anchor="center", x=70, y=55)
        text = tk.Text(forth_window, width=15, height=1, bg="lightgrey")
        text.place(anchor="center", x=70, y=78)

        def fibonacci(n):
            fib = [0, 1]
            for i in range(2, n):
                fib.append(fib[-1] + fib[-2])
            return fib[:n]

        def primes(n):
            result = []
            num = 2
            while len(result) < n:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    result.append(num)
                num += 1
            return result

        def squares(n):
            return [i * i for i in range(1, n + 1)]

        def cubes(n):
            return [i ** 3 for i in range(1, n + 1)]

        def compute_sequence(name, count=1):
            if name == "Фибоначи":
                return fibonacci(count)
            elif name == "Простые":
                return primes(count)
            elif name == "Квадраты":
                return squares(count)
            elif name == "Кубы":
                return cubes(count)
            else:
                return []

        def update_text():
            seq_name = var_seq.get()
            count_str = text.get("1.0", "end-1c").strip()
            if not count_str.isdigit() or int(count_str) <= 0:
                text_field.config(state="normal")
                text_field.delete("1.0", tk.END)
                text_field.insert(tk.END, "Введите число")
                text_field.config(state="disabled")
                return

            count = int(count_str)
            seq_values = compute_sequence(seq_name, count)
            seq_str = ", ".join(str(x) for x in seq_values)
            text_field.config(state="normal")
            text_field.delete("1.0", tk.END)
            text_field.insert(tk.END, seq_str)
            text_field.config(state="disabled")

        radio_frame = tk.Frame(forth_window)
        radio_frame.pack(pady=5)

        for seq_name in ["Фибоначи", "Простые", "Квадраты", "Кубы"]:
            rb = tk.Radiobutton(radio_frame, text=seq_name, variable=var_seq, value=seq_name,
                                command=update_text, font=("Arial", 12))
            rb.pack(anchor="w")

        text_field = tk.Text(forth_window, height=4, width=40, font=("Arial", 12), bg="lightgrey")
        text_field.pack(padx=10, pady=10)
        update_text()
        btn_open_forth.config(text="Close Fourth Window")
    else:
        forth_window.destroy()
        forth_window = None
        btn_open_forth.config(text="Open Fourth Window")

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
btn_root_destroy = tk.Button(root, text="Close", command=close_root, width=20, height=2, bg="lightgrey")
btn_root_destroy.place(anchor="center", x=200, y=230)

root.tk.mainloop()
