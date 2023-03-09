board = [[1, 2, 3 ,4, 5, 6],[2, 4, 6, 7, 8, 8],[2, 4, 6, 7, 8, 8],[2, 4, 6, 7, 8, 8]]

check = []

for j in range(len(board)):
    check.append(board[j][3])

for i in check:
    if [i] == [i + 1] == [i + 2] == [i + 3]:
        if [i] != '-':
            if chip_type == 'x':
                print('Player 1 won the game!')
            else:
                print('Player 2 won the game!')
                return True
        



        
