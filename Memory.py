import tkinter as tk
import random
from tkinter import messagebox

def win():
    messagebox.showinfo("Memory Match", "You found every pair!")
    play_again.grid(row=4, column=0, columnspan=4)

window = tk.Tk()
window.title("Memory Match")

symbols = ["A", "B", "C", "D", "E", "F", "G", "H"]
cards = symbols * 2
random.shuffle(cards)
buttons = []
matches = 0

first = None
locked = False

def flip(index):
    global first, locked, matches
    if locked or index == first or buttons[index]["state"] == "disabled":
        return

    buttons[index].config(text=cards[index])

    if first is None:
        first = index
    elif cards[first] == cards[index]:
        buttons[first].config(state="disabled")
        buttons[index].config(state="disabled")
        first = None
        matches += 1
        if matches == len(symbols):
            win()
    else:
        locked = True
        window.after(800, hide, first, index)

def hide(a, b):
    global first, locked
    buttons[a].config(text="?")
    buttons[b].config(text="?")
    first = None
    locked = False

def reset():
    global first, locked, matches
    random.shuffle(cards)
    for b in buttons:
        b.config(text="?", state="normal")
    first = None
    locked = False
    matches = 0
    play_again.grid_remove()


for row in range(4):
    for col in range(4):
        button = tk.Button(window, text="?", width=6, height=3,
                   command=lambda i=len(buttons): flip(i))
        button.grid(row=row, column=col)
        buttons.append(button)
play_again = tk.Button(window, text="Play Again", command=reset)
window.mainloop()