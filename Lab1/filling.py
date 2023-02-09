import random

field = []
o = '0'
x = 'X'
m = 5


def check_win(smb):
    for n in range(m):
        for i in range(m):
            check_line(field[n][i], smb)
            #check_line(field[0][n], field[1][n], field[2][n], smb)
    #check_line(field[0][0], field[1][1], field[2][2], smb)
    #check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,smb):
    for n in range(m):
        for i in range(m):
            if a1[n][i]['text'] == smb:
                a1[n][i]['background'] = 'pink'
                global game_run
                game_run = False
    #if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        #a1['background'] = a2['background'] = a3['background'] = 'pink'
        #global game_run
        #game_run = False


def can_win(a1,a2,a3,smb):
    res = False

    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = o
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = o
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = o
        res = True
    return res

def computer_move():
    for n in range(m):
        for i in range(m):
            if can_win(field[n][i], o):
                return
    #if can_win(field[0][0], field[1][1], field[2][2], o):
        #return
    #if can_win(field[2][0], field[1][1], field[0][2], o):
        #return
    for n in range(m):
        for i in range(m):
            if can_win(field[n][i], x):
                return
    #if can_win(field[0][0], field[1][1], field[2][2], x):
        #return
    #if can_win(field[2][0], field[1][1], field[0][2], x):
        #return
    while True:
        row = random.randint(0, m-1)
        col = random.randint(0, m-1)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = o
            break