from tkinter import Tk, LabelFrame, Text, Entry, W, E, S, N, \
    Button, Label, PhotoImage, RAISED
import numpy as np

root = Tk()
root.geometry('+10+10')
root.title('Chess')
# root.iconphoto(True, PhotoImage(file='ico.png'))

lf = LabelFrame(root, relief=RAISED, bd=20, bg='gray')
lf.grid(row=0, column=0, sticky=W + E, padx=4)
lf2 = LabelFrame(root, bd=0)
lf2.grid(row=1, column=0, sticky=W + E)
text = Text(lf2, font='arial 14', width=0, height=0)
text.pack(fill='both')
text.tag_configure('tag-center', justify='center')
entry = Entry(lf2, font='arial 16 bold', justify='center')
entry.pack(fill='both')
block = [False]

COLORS = ('gold', 'coral3', 'gray90')
player = ["White's", "Black's"]
dl = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
dn = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

wp, bp = "\u2659", "\u265F"
wr, br = "\u2656", "\u265C"
wk, bk = "\u2658", "\u265E"
wb, bb = "\u2657", "\u265D"
wq, bq = "\u2655", "\u265B"
wK, bK = "\u2654", "\u265A"
s, sp = ' ' * 3, ' ' * 4

chessman = np.array([
    [s, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', s],
    [8, br, bk, bb, bq, bK, bb, bk, br, 8],
    [7, bp, bp, bp, bp, bp, bp, bp, bp, 7],
    [6, sp, sp, sp, sp, sp, sp, sp, sp, 6],
    [5, sp, sp, sp, sp, sp, sp, sp, sp, 5],
    [4, sp, sp, sp, sp, sp, sp, sp, sp, 4],
    [3, sp, sp, sp, sp, sp, sp, sp, sp, 3],
    [2, wp, wp, wp, wp, wp, wp, wp, wp, 2],
    [1, wr, wk, wb, wq, wK, wb, wk, wr, 1],
    [s, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', s]
], dtype=str)


def message(txt, clr):
    text.delete(1.0, 'end')
    text.insert(1.0, txt, 'tag-center')
    text.configure(fg=clr)


def main(e=None):
    move = entry.get()
    entry.delete(0, 'end')
    entry.focus()
    message(f'{player[0]} move, for example e2e4', 'green')
    if block[0]:
        try:
            if dl[move[0]] == dl[move[2]] and dn[move[1]] == dn[move[3]]:
                move = ''
            chessman[1:-1, 1:-1][dn[move[3]], dl[move[2]]] = \
                chessman[1:-1, 1:-1][dn[move[1]], dl[move[0]]]
            chessman[1:-1, 1:-1][dn[move[1]], dl[move[0]]] = sp
            player.reverse()
            message(f'{player[0]} move, for example e2e4', 'green')
        except (IndexError, BaseException):
            message(f'Wrong move. {player[0]} move, for example e2e4', 'red')

    for index, value in np.ndenumerate(chessman):
        color = 2 if value not in chessman[1:-1, 1:-1] else (index[0] + index[1]) % 2
        lbl = Label(lf, text=value, background=COLORS[color],
                    font='century 20' if color == 2 else 'arial 30', relief=RAISED)
        lbl.grid(row=index[0], column=index[1], sticky=N + S + W + E)
    block[0] = True


bt = Button(lf2, text='E N T E R', font='century 14 bold', fg='red', bd=4, command=main)
bt.pack(fill='both')
root.bind("<Return>", main)

main()
root.mainloop()
