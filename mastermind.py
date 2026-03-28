import tkinter as tk
from collections import Counter
import random
 
# ── Constants ───────────────────────────────────────────────────
COLOURS      = ['R', 'B', 'G', 'Y']
COLOUR_NAMES = {'R':'Red',     'B':'Blue', 'G':'Green', 'Y':'Yellow'}
COLOUR_HEX   = {'R':'#E74C3C', 'B':'#2980B9', 'G':'#27AE60', 'Y':'#F1C40F'}
NAME_TO_LETTER = {v: k for k, v in COLOUR_NAMES.items()}
PEGS         = 4
MAX_GUESSES  = 8
 
# ── Window ──────────────────────────────────────────────────────
root = tk.Tk()
root.title('Mastermind')
root.resizable(False, False)
 
# ── Game state ──────────────────────────────────────────────────
secret      = [random.choice(COLOURS) for _ in range(PEGS)]
guess_count = 0
game_over   = False
 
# ── Feedback logic ──────────────────────────────────────────────
def get_feedback(secret, guess):
    blacks = sum(g == s for g, s in zip(guess, secret))
    secret_counts = Counter(secret)
    guess_counts  = Counter(guess)
    total_matched = sum(min(secret_counts[c], guess_counts[c]) for c in COLOURS)
    whites = total_matched - blacks
    return blacks, whites
 
# ── Submit guess ────────────────────────────────────────────────
def submit_guess():
    global guess_count, game_over
    if game_over:
        return
    guess = [selections[i].get() for i in range(PEGS)]
    blacks, whites = get_feedback(secret, guess)
    guess_count += 1
    row = guess_count
    tk.Label(history_frame, text=str(guess_count),
             width=8, relief='groove').grid(row=row, column=0)
    for i, letter in enumerate(guess):
        tk.Label(history_frame, text=COLOUR_NAMES[letter],
                 bg=COLOUR_HEX[letter], fg='white',
                 width=8, relief='groove').grid(row=row, column=i+1)
    feedback_text = '⚫'*blacks + '⚪'*whites or '—'
    tk.Label(history_frame, text=feedback_text,
             width=8, relief='groove').grid(row=row, column=PEGS+1)
    if blacks == PEGS:
        status_label.config(text=f'🎉 Cracked in {guess_count} guesses!')
        game_over = True
        reveal_secret()
    elif guess_count >= MAX_GUESSES:
        status_label.config(text='💀 Out of guesses!')
        game_over = True
        reveal_secret()
    else:
        status_label.config(text=f'Guess {guess_count+1} of {MAX_GUESSES}')
 
# ── Reveal secret ───────────────────────────────────────────────
def reveal_secret():
    reveal_frame = tk.Frame(root)
    reveal_frame.grid(row=4, column=0, columnspan=6, pady=4)
    tk.Label(reveal_frame, text='Secret:',
             font=('Arial',11,'bold')).grid(row=0, column=0, padx=5)
    for i, letter in enumerate(secret):
        tk.Label(reveal_frame, text=COLOUR_NAMES[letter],
                 bg=COLOUR_HEX[letter], fg='white',
                 width=8, relief='groove').grid(row=0, column=i+1)
 
# ── New game ────────────────────────────────────────────────────
def new_game():
    global secret, guess_count, game_over
    secret = [random.choice(COLOURS) for _ in range(PEGS)]
    guess_count = 0
    game_over   = False
    for w in history_frame.winfo_children(): w.destroy()
    for i, text in enumerate(['#','Peg 1','Peg 2','Peg 3','Peg 4','Feedback']):
        tk.Label(history_frame, text=text, font=('Arial',11,'bold'),
                 width=8, relief='groove').grid(row=0, column=i)
    for w in root.grid_slaves():
        if int(w.grid_info()['row']) == 4: w.destroy()
    status_label.config(text=f'Guess 1 of {MAX_GUESSES}')
    for s in selections: s.set('R')
 
def on_dropdown_change(name, idx):
    selections[idx].set(NAME_TO_LETTER[name])
 
# ── Widgets ─────────────────────────────────────────────────────
tk.Label(root, text='Mastermind — Crack the 4-colour code!',
         font=('Arial',14,'bold'), pady=8).grid(row=0, column=0, columnspan=6)
 
history_frame = tk.Frame(root)
history_frame.grid(row=1, column=0, columnspan=6, padx=10, pady=5)
for i, text in enumerate(['#','Peg 1','Peg 2','Peg 3','Peg 4','Feedback']):
    tk.Label(history_frame, text=text, font=('Arial',11,'bold'),
             width=8, relief='groove').grid(row=0, column=i)
 
selections = [tk.StringVar(value='R') for _ in range(PEGS)]
input_frame = tk.Frame(root)
input_frame.grid(row=2, column=0, columnspan=6, pady=8)
tk.Label(input_frame, text='Your guess:', font=('Arial',11)).grid(row=0, column=0, padx=5)
for i in range(PEGS):
    om = tk.OptionMenu(input_frame, selections[i],
                       *[COLOUR_NAMES[c] for c in COLOURS],
                       command=lambda val, idx=i: on_dropdown_change(val, idx))
    om.config(width=8)
    om.grid(row=0, column=i+1, padx=3)
tk.Button(input_frame, text='Submit Guess', font=('Arial',11),
          command=submit_guess).grid(row=0, column=PEGS+1, padx=10)
 
status_label = tk.Label(root, text=f'Guess 1 of {MAX_GUESSES}',
                        font=('Arial',12), pady=6)
status_label.grid(row=3, column=0, columnspan=6)
 
tk.Button(root, text='New Game', font=('Arial',11),
          command=new_game).grid(row=5, column=0, columnspan=6, pady=6)
 
root.mainloop()

