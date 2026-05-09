import math
from colorama import Fore, Style, init

# Initialize colorama
init()

board = [" " for _ in range(9)]

def print_board():
    print()

    for i in range(3):
        row = ""

        for j in range(3):
            cell = board[i * 3 + j]

            if cell == "X":
                row += Fore.GREEN + "X" + Style.RESET_ALL
            elif cell == "O":
                row += Fore.RED + "O" + Style.RESET_ALL
            else:
                row += str(i * 3 + j + 1)

            if j < 2:
                row += " | "

        print(row)

        if i < 2:
            print("--+---+--")

    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True

    return False

def check_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if check_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

def ai_move():
    best_score = -math.inf
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

def player_move():
    while True:
        try:
            move = int(input(Fore.CYAN + "Enter position (1-9): " + Style.RESET_ALL)) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print(Fore.YELLOW + "Invalid move. Try again." + Style.RESET_ALL)

        except ValueError:
            print(Fore.YELLOW + "Please enter a number." + Style.RESET_ALL)

print(Fore.MAGENTA + "\n=== TIC-TAC-TOE AI ===" + Style.RESET_ALL)
print(Fore.GREEN + "You are X" + Style.RESET_ALL)
print(Fore.RED + "AI is O\n" + Style.RESET_ALL)

while True:
    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print(Fore.GREEN + "🎉 You win!" + Style.RESET_ALL)
        break

    if check_draw():
        print_board()
        print(Fore.CYAN + "It's a draw!" + Style.RESET_ALL)
        break

    print(Fore.RED + "AI is making a move..." + Style.RESET_ALL)

    ai_move()

    if check_winner("O"):
        print_board()
        print(Fore.RED + "🤖 AI wins!" + Style.RESET_ALL)
        break

    if check_draw():
        print_board()
        print(Fore.CYAN + "It's a draw!" + Style.RESET_ALL)
        break