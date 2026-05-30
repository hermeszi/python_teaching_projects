import tkinter as tk
 
# Our four colours -- we use short letters in the code
COLOURS = ['red', 'blue', 'green', 'yellow']
 
root = tk.Tk()
root.title('Mastermind')
 
# This function runs when a colour button is clicked
def pick_colour(colour):
    print('You picked:', colour)
 
def pick_colour(colour):
    if len(guess) < 4:           # only if there is an empty slot
        guess.append(colour)     # add colour to the guess
        slot = slots[len(guess) - 1]   # the slot we just filled
        slot.config(bg=colour)         # colour that box in

def count_blacks(guess, secret):
    blacks = 0
    for i in range(4):
        if guess[i] == secret[i]:   # same colour, same spot
            blacks += 1
    return blacks

def count_pegs(guess, secret):
    # Make copies we can change (cross things off)
    secret_left = list(secret)
    guess_left  = list(guess)
 
    blacks = 0
    whites = 0
 
    # ── STEP 1: find blacks (same colour, same spot) ──
    # Go from the back so removing items doesn't shift positions
    for i in range(3, -1, -1):
        if guess_left[i] == secret_left[i]:
            blacks += 1
            secret_left.pop(i)   # cross off
            guess_left.pop(i)    # cross off
 
    # ── STEP 2: find whites from what is left ──
    for colour in guess_left:
        if colour in secret_left:
            whites += 1
            secret_left.remove(colour)   # cross off so we don't reuse it
 
    return blacks, whites

def check_guess():
    global guesses_used
 
    if len(guess) < 4:
        result_label.config(text='Pick 4 colours first!')
        return
 
    guesses_used += 1
    blacks, whites = count_pegs(guess, secret)
 
    if blacks == 4:
        result_label.config(
            text=f'🎉 You win in {guesses_used} guesses!')
    elif guesses_used >= MAX_GUESSES:
        result_label.config(
            text=f'💀 Out of guesses! Code was {secret}')
    else:
        left = MAX_GUESSES - guesses_used
        result_label.config(
            text=f'Black: {blacks}  White: {whites}   ({left} guesses left)')
 
    clear_guess()   # auto-clear so they can guess again

def clear_guess():
    guess.clear()              # empty the list
    for box in slots:
        box.config(bg='white') # reset all boxes to white
 
# Make one button for each colour
for colour in COLOURS:
    btn = tk.Button(
        root,
        text=colour,
        bg=colour,            # button background = the colour
        width=8, height=2,
        command=lambda c=colour: pick_colour(c)
    )
    btn.pack(side='left', padx=4, pady=10)

# The guess starts empty. It will hold up to 4 colours.
guess = []
 
# A row of 4 boxes to show the current guess
slot_frame = tk.Frame(root)
slot_frame.pack(pady=10)
 
slots = []   # we keep the 4 box-labels here
for i in range(4):
    box = tk.Label(slot_frame, text=' ', bg='white',
                   width=6, height=2, relief='solid', borderwidth=1)
    box.pack(side='left', padx=3)
    slots.append(box)

import random
 
# Pick 4 random colours for the secret. Repeats are allowed.
secret = [random.choice(COLOURS) for _ in range(4)]
 
print('SECRET (for testing):', secret)
# A label to show the clue
result_label = tk.Label(root, text='Pick 4 colours, then Check',
                        font=('Arial', 12))
result_label.pack(pady=8)
 
check_btn = tk.Button(root, text='Check', command=check_guess)
check_btn.pack(pady=4)

clear_btn = tk.Button(root, text='Clear', command=clear_guess)
clear_btn.pack(pady=4)

guesses_used = 0
MAX_GUESSES  = 8

def new_game():
    global secret, guesses_used
    secret = [random.choice(COLOURS) for _ in range(4)]
    guesses_used = 0
    clear_guess()
    result_label.config(text='New game! Pick 4 colours.')
    print('SECRET (for testing):', secret)   # remove later
 
new_btn = tk.Button(root, text='New Game', command=new_game)
new_btn.pack(pady=4)



 
root.mainloop()
























