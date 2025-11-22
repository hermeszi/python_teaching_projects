import tkinter as tk
import random

root = tk.Tk()
root.title("Catch Game")

W = 400
H = 500
canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

basket_w = 80
basket_h = 20
basket_x = W//2
basket_y = H - 40
basket = canvas.create_rectangle(
basket_x - basket_w//2, basket_y - basket_h//2,
basket_x + basket_w//2, basket_y + basket_h//2,
fill="blue"
)

score = 0
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()

obj_r = 20
obj_x = random.randint(20, W-20)
obj_y = 20
falling = canvas.create_oval(obj_x-obj_r, obj_y-obj_r, obj_x+obj_r, obj_y+obj_r, fill="red")

def move_left(event):
    global basket_x
    basket_x -= 20
    canvas.coords(basket, \
    basket_x - basket_w//2, basket_y - basket_h//2,\
    basket_x + basket_w//2, basket_y + basket_h//2)

def move_right(event):
    global basket_x
    basket_x += 20
    canvas.coords(basket,
    basket_x - basket_w//2, basket_y - basket_h//2,
    basket_x + basket_w//2, basket_y + basket_h//2)

root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

def game_loop():
    global obj_y, obj_x, score

    obj_y += 5
    canvas.coords(falling, obj_x-obj_r, obj_y-obj_r,
    obj_x+obj_r, obj_y+obj_r)

    left = basket_x - basket_w//2
    right = basket_x + basket_w//2
    b_top = basket_y - basket_h//2

    if obj_y + obj_r >= b_top and left <= obj_x <= right:
        score += 1
        score_label.config(text=f"Score: {score}")
        obj_x = random.randint(20, W-20)
        obj_y = 20
    
    if obj_y > H:
        obj_x = random.randint(20, W-20)
        obj_y = 20

    root.after(30, game_loop)

game_loop()
root.mainloop()