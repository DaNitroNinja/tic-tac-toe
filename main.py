import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                row, col = divmod(move - 1, 3)
                if board[row][col] == ' ':
                    board[row][col] = player
                    break
                else:
                    print("Cell already occupied. Try again.")
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def computer_move(board, player):
    print("Computer's move:")
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = player
            break

def tic_tac_toe():
    while True:
        mode = input("Choose mode (1 for vs Player, 2 for vs Computer): ")
        if mode in ['1', '2']:
            break
        else:
            print("Invalid mode. Please enter 1 or 2.")

    player1 = 'X'
    player2 = 'O' if mode == '1' else 'Computer'
    scores = {player1: 0, player2: 0}

    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = player1

        while True:
            print_board(board)

            if mode == '1' or current_player == player1:
                player_move(board, current_player)
            else:
                computer_move(board, current_player)

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                scores[current_player] += 1
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = player2 if current_player == player1 else player1

        print(f"Scores - Player X: {scores['X']} | Player O: {scores['O']} | Computer: {scores['Computer']}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    tic_tac_toe()
