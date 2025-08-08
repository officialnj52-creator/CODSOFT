from tkinter import *
import random

game = Tk()
game.title("Rock Paper Scissors")
game.geometry("350x420")
game.resizable(False, False)

bg_img = PhotoImage(file="D:/codes/vs code/images/bg.png")
bg_label = Label(game, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(game, text="Rock - Paper - Scissors", font=("Arial", 16, "bold"),
      fg="#00FFFF", bg="#000000").pack(pady=20)

dispaly = Frame(game, bg="#000000")
dispaly.pack(pady=20)

human = Label(dispaly, text="You: 0", font=("Arial", 12, "bold"),
              bg="#000000", fg="white")
human.grid(row=0, column=0, padx=30)

ai = Label(dispaly, text="Computer: 0", font=("Arial", 12, "bold"),
           bg="#000000", fg="white")
ai.grid(row=0, column=1, padx=30)

output = Label(game, text="", font=("Arial", 13, "bold"), bg="#000000")
output.pack(pady=8)

ai_choice = Label(game, text="", font=("Arial", 11),
                  fg="#FFFF39", bg="#000000")
ai_choice.pack()

rock_img = PhotoImage(file="D:/codes/vs code/images/rock.gif")
paper_img = PhotoImage(file="D:/codes/vs code/images/paper.gif")
scissors_img = PhotoImage(file="D:/codes/vs code/images/cutter.gif")

human_score = 0
ai_score = 0

def play(choice):
    global human_score, ai_score
    options = ['rock', 'paper', 'scissors']
    comp = random.choice(options)

    if choice == comp:
        result = "It's a Tie!"
        output.config(fg="gray")
    elif (choice == 'rock' and comp == 'scissors') or \
         (choice == 'paper' and comp == 'rock') or \
         (choice == 'scissors' and comp == 'paper'):
        result = "You Win!"
        output.config(fg="#39FF14")
        human_score += 1
    else:
        result = "Computer Wins!"
        output.config(fg="red")
        ai_score += 1

    output.config(text=result)
    human.config(text=f"You: {human_score}")
    ai.config(text=f"Computer: {ai_score}")
    ai_choice.config(text=f"Computer chose: {comp}")

def reset_game():
    global human_score, ai_score
    human_score = 0
    ai_score = 0
    human.config(text="You: 0")
    ai.config(text="Computer: 0")
    output.config(text="")
    ai_choice.config(text="")

button_dispaly = Frame(game, bg="black")
button_dispaly.pack(pady=25)

Button(button_dispaly, image=rock_img, command=lambda: play("rock"),
       border=0, bg="black", activebackground="black").grid(row=0, column=0, padx=4)
Button(button_dispaly, image=paper_img, command=lambda: play("paper"),
       border=0, bg="black", activebackground="black").grid(row=0, column=1, padx=4)
Button(button_dispaly, image=scissors_img, command=lambda: play("scissors"),
       border=0, bg="black", activebackground="black").grid(row=0, column=2, padx=4)

Button(game, text="Reset Game", font=("Arial", 10, "bold"),
       fg="#FF073A", bg="#0D0D0D", activebackground="#1a1a1a",
       command=reset_game).pack(pady=10)

Label(game, text="Created by Nj", font=("Arial", 9),
      fg="#d3ded3", bg="black").pack(side=BOTTOM, pady=10)

game.mainloop()
