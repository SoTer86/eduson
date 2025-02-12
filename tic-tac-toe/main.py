import colorama


def draw_board(board):
    ...
    

def ask_move(player, board):
    ...


def make_move(player, board, x, y):
    ...

def ask_and_make_move(player, board):
    ask_move()
    make_move()


def check_win(player, board) -> bool:
    ...
    return True


def tic_tac_toe():
    draw_board(board)
    while True:
        ask_and_make_move(player, board)
        check_win(player, board)
        


