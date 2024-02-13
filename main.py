MARKS = ["x", "o"]


def check_winner(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True
    for col in range(board_size):
        if all(board[row][col] == mark for row in range(board_size)):
            return True
    if all(board[i][i] == mark for i in range(board_size)) or all(board[i][board_size-i-1] == mark for i in range(board_size)):
        return True
    return False


def get_current_board():
    board_len = [str(number) for number in range(board_size)]
    print(f"    {'    '.join(board_len)}")
    for _, p in enumerate(playing_board):
        print(f"{_} {p}")


def select_position(mark):
    player_choice = input(f"Player with '{mark}', choose position in format e.g. '01', 1. number is a row and 2. number is a column: ")
    choice_for_check = playing_board[int(player_choice[0])][int(player_choice[1])]
    if choice_for_check == " ":
        playing_board[int(player_choice[0])][int(player_choice[1])] = mark
        get_current_board()
    else:
        print("Already chosen, try again!")
        select_position(mark)


def play_tic_tac_toe():
    global board_size, playing_board

    max_rounds = board_size**2
    get_current_board()
    game_is_over = False
    current_round = 1
    while not game_is_over:
        for i in range(0, 2):
            if current_round <= max_rounds:
                select_position(MARKS[i])
                if check_winner(playing_board, MARKS[i]):
                    print(f"Player with '{MARKS[i]}' wins!")
                    game_is_over = True
                    break
                current_round += 1
            else:
                print("It's a draw, nobody wins.")
                game_is_over = True


if __name__ == '__main__':
    board_size = int(input("Choose board size, e.g. 3 for classic version or more: "))

    playing_board = [[' ' for _ in range(board_size)] for _ in range(board_size)]

    play_tic_tac_toe()
