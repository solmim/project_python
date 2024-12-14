def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    """Checks if the given player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if "" in row:
            return False
    return True
def play_tic_tac_toe():
    """Plays a game of Tic-Tac-Toe."""
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")

        try:
            row, col = map(
                int,
                input(
                    "Введите номер строки и столбца (от 1 до 3, разделенные пробелом): "
                ).split(),
            )
            row -= 1
            col -= 1

            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Неверный ввод. Пожалуйста, введите числа от 1 до 3.")
                continue
            if board[row][col] != "":
                print("Клетка уже занята. Попробуйте еще раз.")
                continue

            board[row][col] = current_player

            if check_win(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите два числа, разделенные пробелом.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    play_tic_tac_toe()