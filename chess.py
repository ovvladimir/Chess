import numpy as np
import os

os.system("")

chessman = {
    "pawn": "\u265F", "rook": "\u265C",
    "kNight": "\u265E", "bishop": "\u265D",
    "queen": "\u265B", "king": "\u265A"}

letters = ' \u0041 \u0042 \u0043 \u0044 \u0045 \u0046 \u0047 \u0048 \n'
c1, c2 = '\x1b[48;5;124m', '\x1b[48;5;172m'
black = '\x1b[30m'
white = '\x1b[97m'
red = '\x1b[91m'
clear = '\x1b[F\x1b[K'
reset = '\x1b[0m'
continues = '\x1b[13F\x1b[J'
player = ["White's", "Black's"]
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
ff = False

dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
chessfield = np.array([
    [br, bk, bb, bq, bK, bb, bk, br],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [wp, wp, wp, wp, wp, wp, wp, wp],
    [wr, wk, wb, wq, wK, wb, wk, wr]
], dtype=object)

chessboard = np.tile(np.array([[c2, c1], [c1, c2]], dtype=object), (4, 4))
chessboard.flags.writeable = False


def main():
    fields = f'{letters}8'
    for index, value in np.ndenumerate(chessboard):
        figure = chessfield[index]
        fields += f'{value}{figure if figure else " "} {reset}{8 - index[0]}\n{7 - index[0]}' \
            if index[1] == 7 else f'{value}{figure if figure else " "} '
    print(fields, f'\r{letters}')

    move = input(f'[q-Exit] {player[0]} move, for example e2e4 -> ')
    if move != 'q':
        try:
            index = [int(j) * -1 if i % 2 != 0 else dic[j] for i, j in enumerate(move)]
            chessfield[index[3], index[2]] = chessfield[index[1], index[0]]
            chessfield[index[1], index[0]] = ff
            player.reverse()
        except (IndexError, BaseException):
            input(f'{clear}{red}wrong move, press enter{reset}')
    else:
        print(f'\n{continues}{reset}[EXIT]')
        return
    print(continues)
    main()


if __name__ == "__main__":
    main()
