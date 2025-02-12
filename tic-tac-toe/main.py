import random
import colorama


MATRIX = 3
LIST_X0 = ['X', '0']


def init_player():
    player = input('За кого будете играть? (X / 0): ')
    if player not in LIST_X0:
        player = ''
        init_player()
    return player


def draw_board(board):
    for i in range(MATRIX):
        for j in range(MATRIX):
            if board[j][i] == 'X':
                print(colorama.Fore.RED + board[j][i], end=' ')
            elif board[j][i] == '0':
                print(colorama.Fore.GREEN + board[j][i], end=' ')
            else:
                print(colorama.Fore.WHITE + board[j][i], end=' ')
        print('')
    

def ask_move(player, board):
    x, y = map(int, input('Введите координаты: ').split())
    if 0 > x > MATRIX or 0 > y > MATRIX:
        ask_move(player, board)
    return x, y


def make_move(player, board, x, y):
    return board[x][y] not in LIST_X0


def ask_and_make_move(player, board):
    while True:
        x, y = ask_move(player, board)
        if make_move(player, board, x, y):
            break
        print("Координаты заняты, повторите ввод.")
    board[x][y] = player
    return board


def check_win(player, board) -> bool:
    if (board[0][0] == player and board[0][1] == player and board[0][2] == player) or \
        (board[1][0] == player and board[1][1] == player and board[1][2] == player) or \
        (board[2][0] == player and board[2][1] == player and board[2][2] == player) or \
        \
        (board[0][0] == player and board[1][0] == player and board[2][0] == player) or \
        (board[0][1] == player and board[1][1] == player and board[2][1] == player) or \
        (board[0][2] == player and board[1][2] == player and board[2][2] == player) or \
        \
        (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
        (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    else:
        return False


def count_board(board):
    count = 0
    for i in range(MATRIX):
        count += board[i].count('.')
    return count


def robot_move(player, board):
    robot = '0' if player == 'X' else 'X' 
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if make_move(robot, board, x, y):
            break
    board[x][y] = robot
    return board, robot


def tic_tac_toe():
    board = [['.'] * MATRIX for i in range(MATRIX)]
    player = init_player()
    
    draw_board(board)
    
    while True:
        board = ask_and_make_move(player, board)
        draw_board(board)
        
        if check_win(player, board):
            print("Вы победили!!!")
            break
        
        if count_board(board) == 0:
            print("Ничья!!!")
            break
        
        board, robot = robot_move(player, board)
        print("Ход робота:")
        draw_board(board)
        
        if check_win(robot, board):
            print("Робот победил!!!")
            break
        
        
if __name__ == "__main__":
    
    colorama.init(autoreset=True)
    
    while True:
        tic_tac_toe()
        if input('Ещё раз? (Y/N) ').capitalize() == 'N':
            break
    
    colorama.deinit()