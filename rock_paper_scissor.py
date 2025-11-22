import tkinter as tk
import random

root = tk.Tk()
root.title("RPS Game")

title_label = tk.Label(root, text="Rock–Paper–Scissors", font=("Arial", 18))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Result: --", font=("Arial", 14))
result_label.pack(pady=5)

score_label = tk.Label(root, text="You: 0   Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

your_score = 0
comp_score = 0

def play(player):
    global your_score, comp_score
    comp = random.choice(["Rock", "Paper", "Scissors"])

    if player == comp:
        result = "Draw"
    elif (player == "Rock" and comp == "Scissors") or \
         (player == "Paper" and comp == "Rock") or \
         (player == "Scissors" and comp == "Paper"):
        result = "You win!"
        your_score += 1
    else:
        result = "You lose!"
        comp_score += 1

    result_label.config(text=f"Result: {player} vs {comp} → {result}")
    score_label.config(text=f"You: {your_score}   Computer: {comp_score}")

def choose_rock():
    play("Rock")

def choose_paper():
    play("Paper")

def choose_scissors():
    play("Scissors")

rock_btn = tk.Button(root, text="Rock", width=10, command=choose_rock)
paper_btn = tk.Button(root, text="Paper", width=10, command=choose_paper)
scissors_btn = tk.Button(root, text="Scissors", width=10, command=choose_scissors)

rock_btn.pack(pady=5)
paper_btn.pack(pady=5)
scissors_btn.pack(pady=5)

root.mainloop()
