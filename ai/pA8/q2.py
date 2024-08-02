import math

class TicTacToe:
    def __init__(self):
        self.board = [' ']*9
        self.current_player = 'X'

    def print_board(self):
        print("-------------")
        for i in range(3):
            print("|", self.board[i*3], "|", self.board[i*3 + 1], "|", self.board[i*3 + 2], "|")
            print("-------------")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return self.board[line[0]]
        if ' ' not in self.board:
            return 'Draw'
        return None

    def get_available_moves(self):
        return [i for i in range(9) if self.board[i] == ' ']


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.check_winner() is not None:
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, depth - 1, False)
            board.board[move] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in board.get_available_moves():
            board.make_move(move)
            eval = minimax(board, depth - 1, True)
            board.board[move] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for move in board.get_available_moves():
        board.make_move(move)
        eval = minimax(board, 3, False)  # Adjust depth for performance
        board.board[move] = ' '
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move



    winner = game.check_winner()
    if winner:
        if winner == 'Draw':
            print("It's a draw!")
        else:
            print(f"{winner} wins!")
        break
