def hello():
    print("---" * 13)
    print("ИГРА КРЕСТИКИ-НОЛИКИ")
    print("---" * 13)
    print("КАК ИГРАТЬ:")
    print("Крестик ходит первым")
    print("Вам нужно будет ввести координаты X, Y")
    print("X - отвечает за горизонталь")
    print("Y - отвечает за вертикаль")
    print("---" * 13)
    print("УДАЧНОЙ ИГРЫ!!!")
    print("---"*13)


def players_name():
    global player1
    global player2
    print(f"Крестик - {player1}")
    print("")
    print(f"Нолик - {player2}")


board = [[""] * 3 for i in range(3)]


def show_board():
    print(f"   0  1  2 ")
    for i in range(3):
        print(f"{i}| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("-"*14)


def ask_position():
    while True:
        x, y = map(int, input("Введите координаты поля:").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if board[x][y] == "":
                return x, y
            else:
                print("Поле занято")
        else:
            print("Вы ввели координаты вне диапазона")


def restart():
    global board
    if win_checker():
        restart_ = input("Вы хотите сыграть снова - Y - да /N - нет? \n").upper()
        if restart_ == "Y":
            board = [[""] * 3 for i in range(3)]
            replay()
        else:
            print("Пока-пока!")


def gameplay():
    global player1
    global player2
    turn = 0
    while True:
        turn += 1

        show_board()

        if turn % 2 == 1:
            print(f"Ходит {player1}...")
        else:
            print(f"ходит {player2}...")

        x, y = ask_position()

        if turn % 2 == 1:
            board[x][y] = "X"
        else:
            board[x][y] = "O"

        if win_checker():
            break

        if turn == 9:
            show_board()
            print("Победила дружба")
            break


def win_checker():
    global player1
    global player2
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)), ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for cords in win_cord:
        symbols = []
        for i in cords:
            symbols.append(board[i[0]][i[1]])
        if symbols == ["X", "X", "X"]:
            show_board()
            print(f"Победил {player1}!")
            return True
        if symbols == ["O", "O", "O"]:
            show_board()
            print(f"Победил {player2}!")
            return True
    return False


def play():
    hello()
    players_name()
    gameplay()
    restart()


def replay():
    players_name()
    gameplay()
    restart()


player1 = input("Кто будет играть за X? \n")
player2 = input("Кто будет играть за O? \n")
play()
