from tkinter import *
from tkinter.font import *

app = Tk()
app.title("To-Do list By Niranjith")
app.geometry("500x630")
app.resizable(False, False)

nor_font = Font(family="Comic Sans MS", size=20, weight="bold", overstrike=False)
crossed = Font(family="Comic Sans MS", size=20, weight="bold", overstrike=True)

tasks = []
mode = "light"
s = None

title = Label(app, text=" Your To-Do List", font=("Arial", 18, "bold"), fg="blue")
title.pack(pady=1)

dis_area = Frame(app, bd=0, relief=SOLID,highlightbackground="black", highlightcolor="light green", highlightthickness=2)
dis_area.pack(pady=5)
scroll = Scrollbar(dis_area, width=10)
scroll.pack(side=RIGHT, fill=Y)

display = Text(dis_area, width=25, height=10, font=nor_font, yscrollcommand=scroll.set,
               bg="#dedede", fg="black", bd=2, relief=FLAT,
               highlightbackground="black", highlightcolor="light green", highlightthickness=2)
display.pack(side=LEFT)
scroll.config(command=display.yview)
display.config(insertontime=0)  #Hide cursor

ent = Label(app, text="Enter your task", font=("Arial", 10, "bold"), fg="blue", bg="SystemButtonFace")
ent.pack(pady=1)

box = Entry(app, font=("Arial", 16), width=25,
            bg="light grey", fg="black", bd=2, relief=SOLID,
            highlightthickness=2, highlightbackground="black", highlightcolor="light green")
box.pack(pady=10)

Label(app, text="Created by Nj", font=("Arial", 8), fg="gray").pack(side=BOTTOM, pady=5)

def refresh():
    display.config(state=NORMAL)
    display.delete(1.0, END)
    for i, task in enumerate(tasks):
        tag = f"task{i}"
        display.insert(END, f"{i+1}. {task[0]}\n", tag)
        if task[1] == "done":
            display.tag_config(tag, font=crossed, foreground="gray")
        else:
            fg = "navy" if mode == "light" else "light blue"
            display.tag_config(tag, font=nor_font, foreground=fg)       
    display.config(state=DISABLED)  #disable tying 
    display.tag_config("selected", background="light green", foreground="white") 

def add_function():
    task = box.get()
    if task:
        tasks.append([task, "no"])
        box.delete(0, END)
        refresh()

def delt_function():
    global s
    try:
        if s is not None:
            tasks.pop(s)
            s = None
            refresh()
            toggle.config(text="Mark as Done", bg="blue")
    except:
        pass

def toggle_done():
    global s
    try:
        if s is not None:
            if tasks[s][1] == "done":
                tasks[s][1] = "no"
            else:
                tasks[s][1] = "done"
            refresh()
            update_button()
    except:
        pass

def update_button():
    global s
    try:
        if s is not None:
            if tasks[s][1] == "done":
                toggle.config(text="Undo Done", bg="orange")
            else:
                toggle.config(text="Mark as Done", bg="blue")
    except:
        toggle.config(text="Mark as Done", bg="blue")

def on_click(event):
    global s
    try:
        display.tag_remove("selected", "1.0", END) 
        s = int(display.index("@%d,%d" % (event.x, event.y)).split('.')[0]) - 1
        l_start = f"{s+1}.0"
        l_end = f"{s+2}.0"
        display.tag_add("selected", l_start, l_end)
        display.tag_raise("selected")
        update_button()
    except:
        pass


def switch_mode():
    global mode
    if mode == "light":     #dark mode black
        app.config(bg="black")
        title.config(fg="light blue", bg="black")
        display.config(bg="gray20", fg="systembuttonface", insertbackground="red",
                       bd=2, relief=SOLID, highlightbackground="white", highlightcolor="light green", highlightthickness=2)
        box.config(bg="gray30", fg="Systembuttonface", insertbackground="white",
                   highlightbackground="white", highlightcolor="light green", highlightthickness=2)
        add.config(bg="seagreen", fg="white")
        delt.config(bg="indian red", fg="white")
        toggle.config(bg="dodger blue", fg="white")
        theme_btn.config(bg="white", fg="black", text="Light Mode")
        ent.config(bg="black")
        mode = "dark"
    else:               #ligth mode black
        app.config(bg="SystemButtonFace")
        title.config(fg="blue", bg="SystemButtonFace")
        display.config(bg="Systembuttonface", fg="black", insertbackground="black",
                       bd=2, relief=SOLID, highlightbackground="black", highlightcolor="light green", highlightthickness=2)
        box.config(bg="light grey", fg="black", insertbackground="black",
                   highlightbackground="black", highlightcolor="light green", highlightthickness=2)
        add.config(bg="green", fg="white")
        delt.config(bg="red", fg="white")
        toggle.config(bg="blue", fg="white")
        theme_btn.config(bg="black", fg="white", text="Dark Mode")
        ent.config(bg="systembuttonface")
        mode = "light"
    refresh()

display.bind("<Button-1>", on_click)

btns = Frame(app)
btns.pack(pady=5)

add = Button(btns, text="Add Task", command=add_function, bg="green", fg="white", font=("Arial", 10, "bold"))
delt = Button(btns, text="Delete", command=delt_function, bg="red", fg="white", font=("Arial", 10, "bold"))
toggle = Button(btns, text="Mark as Done", command=toggle_done, bg="blue", fg="white", font=("Arial", 10, "bold"))

add.grid(row=0, column=0)
delt.grid(row=0, column=1, padx=10)
toggle.grid(row=0, column=2, columnspan=10)

theme_btn = Button(app, text="Dark Mode", command=switch_mode, bg="black", fg="white", font=("Arial", 10, "bold"))
theme_btn.pack(pady=5)

app.mainloop()
