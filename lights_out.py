import tkinter as tk
import random
 
root = tk.Tk()
root.title('Lights Out')
 
ROWS = 5
COLS = 5
 
grid    = [[0] * COLS for _ in range(ROWS)]
buttons = []
 
# ── Core logic ─────────────────────────────────────────────────
 
def toggle_cell(r, c):
    if 0 <= r < ROWS and 0 <= c < COLS:
        grid[r][c] = 1 - grid[r][c]
        colour = 'yellow' if grid[r][c] == 1 else 'grey20'
        buttons[r * COLS + c].config(bg=colour)
 
def on_click(r, c):
    toggle_cell(r,     c)
    toggle_cell(r - 1, c)
    toggle_cell(r + 1, c)
    toggle_cell(r,     c - 1)
    toggle_cell(r,     c + 1)
    check_win()
 
def check_win():
    for row in grid:
        for cell in row:
            if cell == 1:
                return
    status_label.config(text='You WIN! All lights are OFF!')
 
def make_handler(r, c):
    def handler():
        on_click(r, c)
    return handler
 
def shuffle_board(clicks=10):
    for _ in range(clicks):
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        on_click(r, c)
 
def restart():
    global grid
    grid = [[0] * COLS for _ in range(ROWS)]
    for r in range(ROWS):
        for c in range(COLS):
            buttons[r * COLS + c].config(bg='grey20')
    status_label.config(text='Turn all lights OFF!')
    shuffle_board(10)
 
# ── Widgets ─────────────────────────────────────────────────────
 
for r in range(ROWS):
    for c in range(COLS):
        btn = tk.Button(root, width=6, height=3, bg='grey20',
                        command=make_handler(r, c))
        btn.grid(row=r, column=c, padx=2, pady=2)
        buttons.append(btn)
 
status_label = tk.Label(root, text='Turn all lights OFF!',
                        font=('Arial', 14))
status_label.grid(row=ROWS, column=0, columnspan=COLS, pady=10)
 
restart_btn = tk.Button(root, text='New Game',
                        font=('Arial', 12), command=restart)
restart_btn.grid(row=ROWS + 1, column=0, columnspan=COLS, pady=5)
 
# ── Start ───────────────────────────────────────────────────────
 
shuffle_board(10)
root.mainloop()

