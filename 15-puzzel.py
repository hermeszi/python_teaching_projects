import tkinter as tk
import random


SIZE = 80
ROWS = 4
COLS = 4

WIDTH = COLS * SIZE
HEIGHT = ROWS * SIZE

board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,0]
]

def draw_tile(r, c):
    x1 = c * SIZE
    y1 = r * SIZE
    x2 = x1 + SIZE
    y2 = y1 + SIZE

    value = board[r][c]

    # draw background
    if value == 0:
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="gray")
        return

    canvas.create_rectangle(x1, y1, x2, y2, fill="skyblue", outline="gray")

    # draw number in the middle
    canvas.create_text(x1 + SIZE//2,  y1 + SIZE//2, text=str(value), font=("Arial", 24))

def draw_board():
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            draw_tile(r, c)

root = tk.Tk()
root.title("15 Puzzle")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


draw_board()

root.mainloop()

