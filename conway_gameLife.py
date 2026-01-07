import tkinter as tk
import random

#VALUES
ROWS = 40
COLS = 80
CELL_SIZE = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

#------==============Window======================
root = tk.Tk()
root.title("Conway's Game of Life")
root.geometry(f"{WIDTH}x{HEIGHT + 50}")
#-----
#-----===============Board======================
#-----
#0 = dead
#1 = alive

def make_new_board():
    board = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            row.append(0)
        board.append(row)
    return board

def randomize_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = random.choice([0, 0, 0, 1])
    draw_board()

def toggle_cell(c, r):
    board[r][c] = 1 - board[r][c]
    draw_board()

#-----
#-----===============Draw======================
#-----

def draw_cell(c, r):
    color = "black" if board[r][c] == 1 else "white"
    x1 = c * CELL_SIZE
    y1 = r * CELL_SIZE
    x2 = x1 + CELL_SIZE
    y2 = y1 + CELL_SIZE
    canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            draw_cell(c, r)

def clear_board():
    for r in range(ROWS):
        for c in range(COLS):
            board[r][c] = 0
    draw_board()

#-----
#-----===============LOGIC======================
#-----
def count_neighbours(c, r):
    count = 0
    for dr in [-1, 0, 1]:               # loop through rows
        for dc in [-1, 0, 1]:           # loop through columns
            if (dr == 0 and dc == 0):   # skip the current cell
                continue
            nr, nc = r + dr, c + dc                 # get the neighbor's row and column
            if 0 <= nr < ROWS and 0 <= nc < COLS:   # check bounds (avoid out-of-bounds)
                count += board[nr][nc]
    return count

def step(event=None):
    global board
    new_board = make_new_board()
    for r in range(ROWS):
        for c in range(COLS):
            neighbours = count_neighbours(c, r)
            if board[r][c] == 1:
                new_board[r][c] = 1 if neighbours in [2, 3] else 0
            else:
                new_board[r][c] = 1 if neighbours == 3 else 0
    board = new_board
    draw_board()

#-----
#-----===============UI======================
#-----

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row=0, column=0, columnspan=3)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0, columnspan=3)

def on_canvas_click(event):
    c = event.x // CELL_SIZE
    r = event.y // CELL_SIZE
    if 0 <= c < COLS and 0 <= r < ROWS:
        toggle_cell(c, r)

randomButton = tk.Button(button_frame, text="Randomize Board", command=randomize_board)
randomButton.grid(row=1, column=0)
stepButton = tk.Button(button_frame, text="Next Generation", command=step)
stepButton.grid(row=1, column=1)
clearButton = tk.Button(button_frame, text="Clear Board", command=clear_board)
clearButton.grid(row=1, column=2)

canvas.bind("<Button-1>", on_canvas_click)
root.bind("<space>", step)

#-----
#-----===============main======================
#-----

board = make_new_board()
draw_board()
root.focus_set()
root.mainloop()
