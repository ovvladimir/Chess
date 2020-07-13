import PySimpleGUIWeb as sg
import numpy as np

COLORS = ('gold', 'brown', 'gray90')
player = ["White's", "Black's"]
dl = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
dn = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}

wp, bp = "\u2659", "\u265F"
wr, br = "\u2656", "\u265C"
wk, bk = "\u2658", "\u265E"
wb, bb = "\u2657", "\u265D"
wq, bq = "\u2655", "\u265B"
wK, bK = "\u2654", "\u265A"
s, sp = ' ', ''

chessman = np.array([
    [s, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', s],
    ['8', br, bk, bb, bq, bK, bb, bk, br, '8'],
    ['7', bp, bp, bp, bp, bp, bp, bp, bp, '7'],
    ['6', sp, sp, sp, sp, sp, sp, sp, sp, '6'],
    ['5', sp, sp, sp, sp, sp, sp, sp, sp, '5'],
    ['4', sp, sp, sp, sp, sp, sp, sp, sp, '4'],
    ['3', sp, sp, sp, sp, sp, sp, sp, sp, '3'],
    ['2', wp, wp, wp, wp, wp, wp, wp, wp, '2'],
    ['1', wr, wk, wb, wq, wK, wb, wk, wr, '1'],
    [s, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', s]
], dtype=str)


def message(txt, clr):
    window['-OUTPUT-'].update(txt, text_color=clr)


def play(move):
    try:
        if (dl[move[0]] == dl[move[2]] and dn[move[1]] == dn[move[3]]) or len(move) != 4 or \
           (9824 > ord(chessman[1:-1, 1:-1][dn[move[1]], dl[move[0]]]) > 9817 and player[0] == "White's") or \
           (9818 > ord(chessman[1:-1, 1:-1][dn[move[1]], dl[move[0]]]) > 9811 and player[0] == "Black's"):
            move = sp
        chessman[1:-1, 1:-1][dn[move[3]], dl[move[2]]] = chessman[1:-1, 1:-1][dn[move[1]], dl[move[0]]]
        chessman[1:-1, 1:-1][dn[move[1]], dl[move[0]]] = sp
        player.reverse()
        message(f'{player[0]} move, for example e2e4', 'green')
    except (IndexError, TypeError, BaseException):
        message(f'Wrong move. {player[0]} move', 'red')
    else:
        for index, value in np.ndenumerate(chessman):
            window[index].update(
                value, text_color='white' if value and 9811 < ord(value) < 9818 else 'black')


layout = [[sg.Frame(
    title='', background_color='gray',
    layout=[[sg.Text(
        text=value, size=(2, 1), justification='center',
        border_width=2, pad=(1, 1), key=index, font='arial 14',
        background_color=COLORS[2 if value not in chessman[1:-1, 1:-1] else (index[0] + index[1]) & 1],
        text_color='white' if value and 9811 < ord(value) < 9818 else 'black')
        for index, value in np.ndenumerate(chessman)][i:i + 10] for i in range(0, 100, 10)])],
    [sg.Text(text=f'{player[0]} move, for example e2e4', size=(22, 1), key='-OUTPUT-',
     text_color='green', font='arial 14', background_color='white')],
    [sg.Input(focus=True, size=(22, 1), font='arial 14', justification='center', key='-INPUT-')],
    [sg.Button('Enter', key='button'), sg.Exit()]]

window = sg.Window('Chess', layout, no_titlebar=True)

while True:
    event, values = window.read()
    if event == 'button':
        play(values['-INPUT-'])
        window['-INPUT-'].update('')
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
