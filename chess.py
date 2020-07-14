# terminal
import numpy as np
import os

os.system("")

chessman = {
    "pawn": "\u2659", "rook": "\u2656",
    "kNight": "\u2658", "bishop": "\u2657",
    "queen": "\u2655", "king": "\u2654"}

letters = ' \u0041 \u0042 \u0043 \u0044 \u0045 \u0046 \u0047 \u0048 \n'
c1, c2 = '\x1b[48;5;124m', '\x1b[48;5;172m'
black = '\x1b[30m'
white = '\x1b[97m'
red = '\x1b[91m'
clear = '\x1b[F\x1b[K'
reset = '\x1b[0m'
continues = '\x1b[12F\x1b[J'
player = ["White's", "Black's"]
dl = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
dn = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
print()

wp = f'{white}{chessman["pawn"]}'
bp = f'{black}{chessman["pawn"]}'
wr = f'{white}{chessman["rook"]}'
br = f'{black}{chessman["rook"]}'
wk = f'{white}{chessman["kNight"]}'
bk = f'{black}{chessman["kNight"]}'
wb = f'{white}{chessman["bishop"]}'
bb = f'{black}{chessman["bishop"]}'
wq = f'{white}{chessman["queen"]}'
bq = f'{black}{chessman["queen"]}'
wK = f'{white}{chessman["king"]}'
bK = f'{black}{chessman["king"]}'
sp = ' '

array = np.array([
    [br, bk, bb, bq, bK, bb, bk, br],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [sp, sp, sp, sp, sp, sp, sp, sp],
    [wp, wp, wp, wp, wp, wp, wp, wp],
    [wr, wk, wb, wq, wK, wb, wk, wr]
], dtype=str)

chessboard = np.tile(np.array([[c2, c1], [c1, c2]], dtype=str), (4, 4))
chessboard.flags.writeable = False


def main():
    fields = f'{letters}8'
    for index, value in np.ndenumerate(chessboard):
        figure = array[index]
        fields += f'{value}{figure}{sp}{reset}{8 - index[0]}\n{7 - index[0]}' \
            if index[1] == 7 else f'{value}{figure}{sp}'
    print(fields, f'\r{letters}')

    move = input(f'[q-Exit] {player[0]} move, for example e2e4 -> ')
    if move != 'q':
        try:
            array[dn[move[3]], dl[move[2]]] = array[dn[move[1]], dl[move[0]]]
            array[dn[move[1]], dl[move[0]]] = sp
            player.reverse()
        except (IndexError, BaseException):
            input(f'{clear}{red}wrong move, press enter{reset}')
    else:
        print(f'{continues}{reset}[EXIT]')
        return
    print(continues, end='')
    main()


if __name__ == "__main__":
    main()
