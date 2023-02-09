from tkinter import *
import random
from filling import *

root = Tk()
root.title('Крестики-нолики')
game_run = True
cross_count = 0

def new_game():
    for row in range(m):
        for col in range(m):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 7:
            computer_move()
            check_win('O')


for row in range(m):
    line = []
    for col in range(m):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=m, column=0, columnspan=m, sticky='nsew')
root.mainloop()