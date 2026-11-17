print("""\nПравила игры:
1) Игрок белых ходит большими буквами, игрок черных - маленькими
2) 
\n""")


placements = {'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'q', 'e8': 'k', 'f8': 'b', 'g8': 'n', 'h8': 'r',
              'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
              'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
              'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
              'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
              'a3': '.', 'b3': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.', 'g3': '.', 'h3': '.',
              'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
              'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R'
              }


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def fits(position1, position2):
    if position1 in placements.keys() and position2 in placements.keys():
        return True
    else:
        print('\nОдной из этих клеток нет на шахматной доске! Попробуйте снова')
        return False


def pawn(start, end):
    if (((start[0] != end[0] and placements[end] == '.') or
        (abs(int(end[1]) - int(start[1])) >= 2 and int(start[1]) not in (2, 7))) or
        (placements[end] != '.' and start[0] == end[0])) or \
        (abs(int(end[1]) - int(start[1])) > 2 and int(start[1]) in (2, 7)):
        print('\nТакой ход невозможен! Попробуйте заново')
        return False
    else:
        return True


def bishop(start, end): # слон
    if abs(int(end[1]) - int(start[1])) != abs(letters.index(end[0]) - letters.index(start[0])):
        print('\nТакой ход невозможен! Попробуйте заново')
        return False
    else:
        return True


def knight(start, end): # конь
    dx = abs(int(end[1]) - int(start[1]))
    dy = abs(letters.index(end[0]) - letters.index(start[0]))

    if (dx, dy) not in ((2, 1), (1, 2)):
        print('\nТакой ход невозможен! Попробуйте заново')
        return False
    else:
        return True


def rook(start, end): # ладья
    if start[0] == end[0] or start[1] == end[1]:
        return True
    else:
        print('\nТакой ход невозможен! Попробуйте заново')
        return False


def queen(start, end):
    if (start[0] == end[0] or start[1] == end[1]) or \
        abs(int(end[1]) - int(start[1])) == abs(letters.index(end[0]) - letters.index(start[0])):
        return True
    else:
        print('\nТакой ход невозможен! Попробуйте заново')
        return False


def king(start, end):
    dx = abs(int(end[1]) - int(start[1]))
    dy = abs(letters.index(end[0]) - letters.index(start[0]))

    if (dx, dy) not in ((1, 1), (1, 0), (0, 1)):
        print('\nТакой ход невозможен! Попробуйте заново')
        return False
    else:
        return True


def printBoard(board):
    print('\n')
    print('     A B C D E F G H\n')

    for i in range(8, 0, -1):
        print(str(i) + '    ' + board[f'a{i}'] + ' ' + board[f'b{i}'] + ' ' + board[f'c{i}'] + ' ' + \
              board[f'd{i}'] + ' ' + board[f'e{i}'] + ' ' + board[f'f{i}'] + ' ' + board[f'g{i}'] + \
              ' ' + board[f'h{i}'] + '    ' + str(i))

    print('\n     A B C D E F G H\n')


i = 1


def MoveBoard(board, player):
    global i
    printBoard(placements)
    if player % 2 != 0:
        print('Ход белых')
    else:
        print('Ход черных')
    from_which = input("> С какой позиции делать ход? ").lower().replace(' ', '')
    to_which = input("> На какую позицию сделать ход? ").lower().replace(' ', '')
    if not fits(from_which, to_which):
        valid = False
    elif placements[from_which] in ('p', 'P'):
        valid = pawn(from_which, to_which)
    elif placements[from_which] in ('n', 'N'):
        valid = knight(from_which, to_which)
    elif placements[from_which] in ('b', 'B'):
        valid = bishop(from_which, to_which)
    elif placements[from_which] in ('r', 'R'):
        valid = rook(from_which, to_which)
    elif placements[from_which] in ('q', 'Q'):
        valid = queen(from_which, to_which)
    elif placements[from_which] in ('k', 'K'):
        valid = king(from_which, to_which)
    elif placements[from_which] == '.':
        print('\nТакой ход невозможен! Попробуйте заново')
        valid = False
    else:
        valid = True

    if not valid:
        i -= 1
        return
    placements[to_which] = placements[from_which]
    placements[from_which] = '.'


while True:
    MoveBoard(placements, i)
    i += 1