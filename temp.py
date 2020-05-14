# https://en.wikipedia.org/wiki/ANSI_escape_code#graphics
import os

os.system("")

chessman = {
    "pawn": "\u265F", "rook": "\u265C",
    "kNight": "\u265E", "bishop": "\u265D",
    "queen": "\u265B", "king": "\u265A"}


def chessboard(num):
    bg = '\033[48;5;'
    black = '\033[30m'
    white = '\033[97m'
    reset = '\033[0m'
    fields = '\n \u0041 \u0042 \u0043 \u0044 \u0045 \u0046 \u0047 \u0048\n'
    for x in range(num, 0, -1):
        fields += f'{x}'
        for y in range(num):
            color = 124 if (x + y) % 2 else 172
            chass = False
            if x == 2:
                chass = f'{white}{chessman["pawn"]}'
            if x == 7:
                chass = f'{black}{chessman["pawn"]}'
            if x == 1 and (y == 0 or y == 7):
                chass = f'{white}{chessman["rook"]}'
            if x == 8 and (y == 0 or y == 7):
                chass = f'{black}{chessman["rook"]}'
            if x == 1 and (y == 1 or y == 6):
                chass = f'{white}{chessman["kNight"]}'
            if x == 8 and (y == 1 or y == 6):
                chass = f'{black}{chessman["kNight"]}'
            if x == 1 and (y == 2 or y == 5):
                chass = f'{white}{chessman["bishop"]}'
            if x == 8 and (y == 2 or y == 5):
                chass = f'{black}{chessman["bishop"]}'
            if x == 1 and y == 3:
                chass = f'{white}{chessman["queen"]}'
            if x == 8 and y == 3:
                chass = f'{black}{chessman["queen"]}'
            if x == 1 and y == 4:
                chass = f'{white}{chessman["king"]}'
            if x == 8 and y == 4:
                chass = f'{black}{chessman["king"]}'
            fields += f'{bg}{color}m{chass if chass else " "} '
        fields += f'{reset}\n'
    return fields


prt = chessboard(8)
print(prt)

if os.name == 'nt':
    import msvcrt
    print('Для выхода нажмите любую клавишу')
    _key_ = ord(msvcrt.getch())
    if _key_:
        print('[ВЫХОД]')
