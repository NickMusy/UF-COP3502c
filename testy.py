def main():

    # Initialize the chip type as 'x' and the player as 'Player 1'
    chip_type = 'x'
    player = 'Player 1: '

    # Ask the user for the number of rows and columns for the board and initialize the board
    rows = int(input('What would you like the height of the board to be? '))
    cols = int(input('What would you like the length of the board to be? '))
    current_board = initialize_board(rows, cols)

    # Print the initial board and the instructions for the players
    print_board(current_board)
    print('''

Player 1: x
Player 2: o

    ''')

    # Loop through the game until someone wins or the board is full
    while True:

        # Ask the current player which column they want to choose and insert their chip in the board
        col_choice = int(input(player + 'Which column would you like to choose? '))
        chip_row = insert_chip(current_board, col_choice, chip_type)

        # Update the board with the current player's chip and print the updated board
        current_board[chip_row][col_choice] = chip_type
        print_board(current_board)
        print()

        # Check if the current player has won the game, and exit the loop if they have
        if check_if_winner(current_board, col_choice, chip_row, chip_type) == True:
            exit()

        # Switch to the other player's turn
        if chip_type == 'x':
            chip_type = 'o'
            player = 'Player 2: '
        else:
            chip_type = 'x'
            player = 'Player 1: '


def initialize_board(num_rows: int, num_columns: int):

    # Initialize a two-dimensional list with '-' in every position
    my_array = [[] for _ in range(num_rows)]
    for i in range(num_rows):
        my_array[i] = ['-'] * num_columns

    return (my_array)


def print_board(board: list):

    # Loop through the board from the top row to the bottom row and from the left column to the right column,
    # and print each position in the board separated by a space
    for i in range((len(board)-1), -1, -1):
        for j in range(len(board[0])):
            print(board[i][j], end=' ')
        print()


def insert_chip(board: list, col: int, chip_type: str):

    # Loop through the rows of the chosen column, and insert the current player's chip in the lowest empty position
    for i in range(len(board)):
        if board[i][col] == '-':
            board[i][col] = chip_type
            break
    return (i)


def check_if_winner(board: list, col: int, row: int, chip_type: str):

    # Check for a win in the rows of the board
    for j in board:
        for i in range(len(j)-3):
            if j[i] == j[i + 1] == j[i + 2] == j[i + 3]:
                if j[i] != '-':
                    if chip_type == 'x':
                        print('Player 1 won the game!')
                    else:
                        print('Player 2 won the game!')
                    return True

    # Check for a win in the columns of the board
    check = []
    lw = True
    if row >= 3:
        for j in range(row,row-4,-1):
            check.append(board
