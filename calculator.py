from tkinter import *
from tkinter import ttk
from tkinter.font import Font

# Hindi digit
hindi_digits = {
    '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
    '5': '५', '6': '६', '7': '७', '8': '८', '9': '९',
    '.': '.', '+': '+', '-': '-', '*': '*', '/': '/', '^': '^',
    'Del': 'हटाएँ', 'AC': 'साफ़ करें', '=': '='
}

def convertor(text):
    return ''.join(hindi_digits.get(ch, ch) for ch in text)

calcs = Tk()
calcs.title("Calculator")
calcs.geometry("340x380")
calcs.resizable(False, False)

lang = StringVar(value="english")

main_font = Font(family="Arial", size=22, weight="bold")
sub_font = Font(family="Arial", size=12)

# Menu bar
menubar = Menu(calcs)
langmenu = Menu(menubar, tearoff=0)
langmenu.add_radiobutton(label="English", variable=lang, value="english", command=lambda: refresh_btn())
langmenu.add_radiobutton(label="Hindi", variable=lang, value="hindi", command=lambda: refresh_btn())
menubar.add_cascade(label="Language", menu=langmenu)
calcs.config(menu=menubar)

Label(calcs, text="Bilingual Calculator", font=("Arial", 14, "bold"), fg="black").pack(pady=(8, 0))

disp_area = Frame(calcs, bd=2, relief=RIDGE)
disp_area.pack(padx=10, pady=10, fill=X)

sec_disp = Label(disp_area, text="", anchor="e", font=sub_font, bg="white", fg="gray", height=1)
sec_disp.pack(fill=X)
first_disp = Label(disp_area, text="", anchor="e", font=main_font, bg="white", fg="black", height=2)
first_disp.pack(fill=X)

expression = ""

def refresh():
    disp = convertor(expression) if lang.get() == "hindi" else expression
    first_disp.config(text=disp)

def press(key):
    global expression
    expression += str(key)
    refresh()

def clear():
    global expression
    expression = ""
    sec_disp.config(text="")
    refresh()

def delete():
    global expression
    expression = expression[:-1]
    refresh()

def calculate():
    global expression
    try:
        result = str(eval(expression.replace('^', '**')))
        sec_disp.config(text=convertor(expression) if lang.get() == "hindi" else expression)
        expression = result
        refresh()
    except Exception:
        expression = ""
        first_disp.config(text="Error")

# Button layout 
button_labels = [
    ['7', '8', '9', 'Del', 'AC'],
    ['4', '5', '6', '*', '/'],
    ['1', '2', '3', '+', '-'],
    ['0', '.', '^', '=']
]

buttons_dict = {}

style = ttk.Style()
style.configure("Rounded.TButton", font=("Arial", 12), padding=5, relief="flat")

button_frame = Frame(calcs)
button_frame.pack()

for r, row in enumerate(button_labels):
    for c, key in enumerate(row):
        if key == '=':
            b = ttk.Button(button_frame, text=key, style="Rounded.TButton", width=10, command=calculate)
            b.grid(row=r, column=c, columnspan=2, padx=5, pady=5, sticky="we")
        else:
            if key == 'Del':
                cmd = delete
            elif key == 'AC':
                cmd = clear
            else:
                cmd = lambda k=key: press(k)

            b = ttk.Button(button_frame, text=key, style="Rounded.TButton", width=4, command=cmd)
            b.grid(row=r, column=c, padx=5, pady=5)
        buttons_dict[key] = b

def refresh_btn():
    for key, btn in buttons_dict.items():
        if lang.get() == "hindi":
            btn.config(text=hindi_digits.get(key, key))
        else:
            btn.config(text=key)

refresh_btn()

Label(calcs, text="Created by Nj", font=("Arial", 9), fg="gray").pack(side=BOTTOM, pady=2)

calcs.mainloop()
