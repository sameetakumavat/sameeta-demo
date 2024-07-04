# Simple tic tac toe game

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    move_count = 0

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        move = input("Enter your move (1-9): ")

        if move not in [str(i) for i in range(1, 10)]:
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        move = int(move) - 1
        row, col = divmod(move, 3)

        if board[row][col] != " ":
            print("This cell is already taken. Try again.")
            continue

        board[row][col] = current_player
        move_count += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if move_count == 9:
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
