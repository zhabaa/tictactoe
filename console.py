def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    if (board[0][0] == board[1][1] == board[2][2] != " " or
        board[0][2] == board[1][1] == board[2][0] != " "):
        return True

    return False


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for turn in range(9):
        print_board(board)

        row = int(input(f"Игрок {current_player}, введите номер строки (1-3): ")) - 1
        col = int(input(f"Игрок {current_player}, введите номер столбца (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player

            if check_winner(board):
                print_board(board)
                print(f"Игрок {current_player} выиграл!")
                return

            current_player = "O" if current_player == "X" else "X"

        else:
            print("Эта ячейка уже занята! Попробуйте снова.")

    print_board(board)
    print("Ничья!")


tic_tac_toe()
