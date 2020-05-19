from tkinter import Tk, LabelFrame, Text, Entry, W, E, S, N, Button, Label, PhotoImage
import numpy as np

root = Tk()
root.geometry('+10+10')
root.title('Chess')
root.iconphoto(False, PhotoImage(file='ico.png'))

sp = ' ' * 4
num = '8 \n\n7 \n\n6 \n\n5 \n\n4 \n\n3 \n\n2 \n\n1 '
letters = f'  \u0061{sp}\u0062{sp}\u0063{sp}\u0064{sp}\u0065{sp}\u0066{sp}\u0067{sp}\u0068'

lf = LabelFrame(root, text=num, font='century 16 bold', fg='red', labelanchor='w', bd=0)
lf.grid(row=0, column=0, sticky=W + E, padx=4)
lf2 = LabelFrame(root, text=letters, font='century 20 bold', fg='red', labelanchor='n', bd=0)
lf2.grid(row=1, column=0, sticky=W + E)
text = Text(lf2, font='arial 14', width=0, height=0)
text.pack(fill='both')
text.tag_configure('tag-center', justify='center')
entry = Entry(lf2, font='arial 16 bold', justify='center')
entry.pack(fill='both')
block = [False]

COLORS = ('gold', 'coral3')
player = ["White's", "Black's"]
dl = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
dn = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

wp, bp = "\u2659", "\u265F"
wr, br = "\u2656", "\u265C"
wk, bk = "\u2658", "\u265E"
wb, bb = "\u2657", "\u265D"
wq, bq = "\u2655", "\u265B"
wK, bK = "\u2654", "\u265A"

chessman = np.array([
    [br, bk, bb, bq, bK, bb, bk, br],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [wp, wp, wp, wp, wp, wp, wp, wp],
    [wr, wk, wb, wq, wK, wb, wk, wr]
], dtype=str)


def message(txt, clr):
    text.delete(1.0, 'end')
    text.insert(1.0, txt, 'tag-center')
    text.configure(fg=clr)


def main(*args):
    move = entry.get()
    entry.delete(0, 'end')
    entry.focus()
    message(f'{player[0]} move, for example e2e4', 'green')
    if block[0]:
        try:
            chessman[dn[move[3]], dl[move[2]]] = chessman[dn[move[1]], dl[move[0]]]
            chessman[dn[move[1]], dl[move[0]]] = sp
            player.reverse()
            message(f'{player[0]} move, for example e2e4', 'green')
        except (IndexError, BaseException):
            message(f'Wrong move. {player[0]} move, for example e2e4', 'red')

    for index, value in np.ndenumerate(chessman):
        color = (index[0] + index[1]) & 1  # % 2
        lb = Label(lf, text=value, background=COLORS[color], font='arial 30')
        lb.grid(row=index[0], column=index[1], sticky=N + S + W + E)
    block[0] = True


bt = Button(lf2, text='E N T E R', font='century 14 bold', fg='red', bd=4, command=main)
bt.pack(fill='both')
root.bind("<Return>", main)

main()
root.mainloop()
