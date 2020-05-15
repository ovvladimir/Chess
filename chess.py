# font cmd - MS Gothic
import numpy as np
import os

os.system("")

chessman = {
    "pawn": "\u265F", "rook": "\u265C",
    "kNight": "\u265E", "bishop": "\u265D",
    "queen": "\u265B", "king": "\u265A"}
bg = '\x1b[48;5;'
black = '\x1b[30m'
white = '\x1b[97m'
red = '\x1b[91m'
reset = '\x1b[0m'
continues = '\x1b[12F\x1b[J'
player = ["White's", "Black's"]

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
NUM = 8

dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
chessboard = np.array([
    [br, bk, bb, bq, bK, bb, bk, br],
    [bp, bp, bp, bp, bp, bp, bp, bp],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [ff, ff, ff, ff, ff, ff, ff, ff],
    [wp, wp, wp, wp, wp, wp, wp, wp],
    [wr, wk, wb, wq, wK, wb, wk, wr]
], dtype=object)
print()


def main():
    fields = ' \u0041 \u0042 \u0043 \u0044 \u0045 \u0046 \u0047 \u0048\n'
    for x in range(NUM, 0, -1):
        fields += f'{x}'
        for y in range(NUM):
            color = 124 if (x + y) % 2 else 172
            figure = ff
            figure = chessboard[x * -1][y]
            fields += f'{bg}{color}m{figure if figure else " "} '
        fields += f'{reset}\n'
    print(fields)
    move = input(f'[q-Exit] {player[0]} move, for example e2e4 -> ')
    if move != 'q':
        try:
            index = [int(j) * -1 if i % 2 != 0 else dic[j] for i, j in enumerate(move)]
            chessboard[index[3], index[2]] = chessboard[index[1], index[0]]
            chessboard[index[1], index[0]] = ff
            player.reverse()
        except BaseException:
            input(f'\x1b[F\x1b[K{red}wrong move, press enter{reset}')
    else:
        print(f'\n{continues}{reset}[EXIT]')
        return
    print(continues)
    main()


if __name__ == "__main__":
    main()
