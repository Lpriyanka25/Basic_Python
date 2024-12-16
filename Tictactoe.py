board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
p1s = 'X'
p2s = 'O'

def checkRows(symbol):  
    for i in range(3):
        count = 0
        for j in range(3):
            if board[i][j] == symbol:
                count += 1
        if count == 3:
            print(symbol, 'won')
            return True
    return False

def checkColumns(symbol):
    for i in range(3):
        count = 0
        for j in range(3):
            if board[j][i] == symbol:
                count += 1
        if count == 3:
            print(symbol, 'won')
            return True
    return False

def checkDiagonals(symbol):
    # Left-to-right diagonal
    if all(board[i][i] == symbol for i in range(3)):
        print(symbol, 'won')
        return True
    # Right-to-left diagonal
    if all(board[i][2-i] == symbol for i in range(3)):
        print(symbol, 'won')
        return True
    return False

def won(symbol):
    return checkRows(symbol) or checkColumns(symbol) or checkDiagonals(symbol)

def place(symbol):
    for row in board:
        print(' '.join(row))
    while True:
        row = int(input('Enter the row (1-3): '))
        column = int(input('Enter the column (1-3): '))
        if 1 <= row <= 3 and 1 <= column <= 3 and board[row-1][column-1] == '-':
            break
        else:
            print('Invalid entry. Try again.')
    board[row-1][column-1] = symbol

