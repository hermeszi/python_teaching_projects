import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Roller Battle")
root.geometry("400x320")

p1_score = 0
p2_score = 0

title_label = tk.Label(root, text="Dice Roller Battle", font=("Arial", 18))
title_label.pack(pady=10)

p1_label = tk.Label(root, text="Player 1: --", font=("Arial", 12))
p1_label.pack(pady=5)

p2_label = tk.Label(root, text="Player 2: --", font=("Arial", 12))
p2_label.pack(pady=5)

score_label = tk.Label(root, text="Score – P1: 0   P2: 0", font=("Arial", 12))
score_label.pack(pady=5)

result_label = tk.Label(root, text="Click ROLL to start", font=("Arial", 12))
result_label.pack(pady=10)

roll_btn = tk.Button(root, text="ROLL", width=12)
roll_btn.pack(pady=5)

def roll_once():
    global p1_score, p2_score

    p1 = random.randint(1, 6)
    p2 = random.randint(1, 6)

    p1_label.config(text=f"Player 1: {p1}")
    p2_label.config(text=f"Player 2: {p2}")

    if p1 > p2:
        p1_score += 1
        result_label.config(text="Player 1 wins this round!")
    elif p2 > p1:
        p2_score += 1
        result_label.config(text="Player 2 wins this round!")
    else:
        result_label.config(text="It's a draw!")

    score_label.config(text=f"Score – P1: {p1_score}   P2: {p2_score}")

    if p1_score >= 3 or p2_score >= 3:
        if p1_score > p2_score:
            result_label.config(text="Player 1 wins the match!")
        elif p2_score > p1_score:
            result_label.config(text="Player 2 wins the match!")
        roll_btn.config(state="disabled")

def roll_button_pressed():
    roll_once()

roll_btn.config(command=roll_button_pressed)

def reset_match():
    global p1_score, p2_score
    p1_score = 0
    p2_score = 0

    p1_label.config(text="Player 1: --")
    p2_label.config(text="Player 2: --")
    score_label.config(text="Score – P1: 0   P2: 0")
    result_label.config(text="Click ROLL to start")
    roll_btn.config(state="normal")

reset_btn = tk.Button(root, text="Reset Match", width=12, command=reset_match)
reset_btn.pack(pady=5)

root.mainloop()
