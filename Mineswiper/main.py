# import needed modules;
import random
import re
# create a board class;


class Board():
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
    # let's create the board;

    # helper functions;
        self.board = self.make_new_board()  # plant the bombs
        self.assign_values_to_board()  # the value is the number of bombs around

    # initialize a set to keep track of which locations we've uncovered
    # we'll save (row, col) tuples into this set
        self.dug = set()  # if we dig at 0, 1, then self.dug = {(0, 1)}

    def make_new_board(self):
        # construct a new board and plant the bombs
        # we should construct the list of lists helper

        # generate a new board;
        board = [[None for _ in range(self.dim_size)]
                 for _ in range(self.dim_size)]
    # plant the bombs;
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
        # this means we've actually planted a bomb there already
            if board[row][col] == '*':
                continue
        # plant a bomb then increment
            board[row][col] = '*'  # plant the bomb
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        # assign a number 0-8 for all empty spaces represents
        # how many neighboring bombs there are.
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                # don't overwrite a bomb
                if self.board[r][c] == '*':
                    continue

                # let a function to check
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)
    # let create the get_num_neighboring_bombs;

    def get_num_neighboring_bombs(self, row, col):
        # let's iterate through each of the neighboring positions and sum the number of bombs
        num_neighboring_bombs = 0
    # possible configurations
    # make sure not to get out off bounds of the board
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if r == row and c == col:
                    # don't check
                    continue
                if self.board[r][c] == '*':
                    # neighboring bomb
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dig at that location
        # return true if successful dig, false if bomb dug
        self.dug.add((row, col))  # keep track of dug positions
        # if we dig a bomb game over
        if self.board[row][col] == '*':
            return False
        # bombs are around
        elif self.board[row][col] > 0:
            return True
        # no bombs around dig more
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r, c) in self.dug:
                    continue  # don't dig where you've already dug
                self.dig(r, c)
        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb here
        return True

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(
            self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
# define play function;


def play(dim_size=10, num_bombs=10):
    # create the board and plant the bombs;
    board = Board(dim_size, num_bombs)
    # show the user the board and ask for where they want to dig;

    # if location is a bomb, show game over message;
    # if location is not a bomb, dig recursively until each
    # square is at least next to a bomb;
    # repeat steps 2/3 until there no more places to dig-->victory;
    safe = True
    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        # split the string when detect any of ',(\\s)*'
        user_input = re.split(
            ',(\\s)*', input("Where would you like to dig? Input as row,col:"))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Try again.")
            continue
        # if it's valid, we dig
        safe = board.dig(row, col)
        # we dug a bomb
        if not safe:
            break
    # you win
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOS!")
    else:
        print("SORRY GAME OVER :(")
        # lets reval the whole board
        board.dug = [(r, c) for r in range(board.dim_size)
                     for c in range(board.dim_size)]
        print(board)


if __name__ == '__main__':  # good practice
    play()
