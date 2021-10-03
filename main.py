import random

brd = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

#player move
def enter_move(board):
    move = int(input("What is your move?"))
    if move is int and 10 > move > 0:
        for y in range(len(board)):
            for x in range(len(board[y])):
                if int(board[y][x]) == int(move):
                    brd[y][x] = "O"
                else:
                    print("Spot is taken, try again")
                    enter_move(brd)
    else:
        print("Not a valid input, try again")
        enter_move(brd)

def make_list_of_free_fields(board):
    free_fields = []
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] is int:
                free_fields += (x, y)
    return free_fields

def victory_for(board, sign):
    #checks rows
    if board[0] == [sign, sign, sign] or board[1] == [sign, sign, sign] or board[2] == [sign, sign, sign]:
        return True
    #checks col
    if (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) \
            or (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) \
            or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign):
        return True
    #checks diag
    if(board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) \
        or (board[0][2] == sign and board[1][1] == sign and board[2][0]):
            return True
    return False

# cpu move
def draw_move(board):
    move = random.randint(1, 7)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if int(board[y][x]) == int(move):
                brd[y][x] = "X"
            else:
                draw_move(brd)


def tie_test(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] is int:
                return False
    return True


display_board(brd)
while not tie_test(brd):
    enter_move(brd)
    display_board(brd)
    if victory_for(brd, "O"):
        break

    if tie_test(brd):
        break

    draw_move(brd)
    display_board(brd)
    if victory_for(brd, "X"):
        break
print("Good game!")

