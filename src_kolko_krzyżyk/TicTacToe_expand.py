class TicTacToe:
    '''Simple game for two person in Tic Tac Toe.
     Player decides how big the board is. Valid board (2 to n)
     where board are matrix n x n. Good Luck and Have Fun.'''

    def __init__(self, martix ,min_deletions = 3):
        self.matrix = martix
        self.board = self.prepare_board()
        self.used_nums = ['' for _ in range(martix*martix)]
        self.way_to_win = []
        self.min_length_deletions = min_deletions

    def printer(self, board):
        '''print board with positions to choose'''
        pattern = ' {}{}|'.format('{}', ' ')
        for i in range(len(board)):
            s = ''.join(pattern.format(str(pos).rjust(len(str(self.matrix**2))))
                        for pos in board[i]).strip('|')
            print(s)
            if i < len(board) - 1:
                print('-' * (len(str(self.matrix ** 2)) + 3) * len(board[i]))
        return ''

    def prepare_board(self):
        '''preparing a board to play - matrix board'''
        if type(self.matrix)!= int:
            raise ValueError
        board = []
        start = 0
        next_numbers = self.matrix
        for arr in range(self.matrix):
            board += [[i for i in range(start, next_numbers)]]
            start += self.matrix
            next_numbers += self.matrix
        return board

    def valid_value(self):
        '''make sure if input value are valid - is digit'''
        while True:
            choice = input('Choose field 0-{}: '.format(len(self.used_nums) - 1))
            try:
                choice = int(choice)
                return choice
            except:
                print('only numbers please')


    def instert_to_board(self, player, player_choice):
        '''inserting player to board return update board '''
        if 0 <= player_choice <= len(self.used_nums):
            if self.used_nums[player_choice] == '':
                counter = 0
                for arr in self.board:
                    for i in range(len(arr)):
                        if player_choice == counter:
                            arr[i] = 'X' if player == 0 else 'O'
                            self.used_nums[counter] = player
                        counter += 1
                return self.board
            else:
                print('Field {} are occupied try again'.format(player_choice))
        else:
            print('Wrong choice {} try again. Allow chooses 0-{}'.format
                      (player_choice, len(self.used_nums) - 1))


    def draw(self):
        '''when all fild are occupied in used_nums return True'''
        return all(1 if ele != '' else 0 for ele in self.used_nums)

    def horizontal_win(self, board):
        '''check when we have few same signs in row than return True'''
        player_x, player_o = 0, 0
        for arr in board:
            for num in arr:
                if num == 'X' or num == 'O':
                    if num == 'X':
                        player_x += 1
                        player_o = 0
                    else:
                        player_o += 1
                        player_x = 0
                if player_x >= self.min_length_deletions or player_o >= self.min_length_deletions:
                    return True
            else:
                player_x, player_o = 0, 0
        return False

    def vertical_win(self, board):
        '''check when we have few same signs in column than return True'''
        player_x, player_o = 0, 0
        for c in range(len(board)):
            for arr in board :
                if arr[c] == 'X' or arr[c] == 'O':
                    if arr[c] == 'X':
                        player_x += 1
                        player_o = 0
                    else:
                        player_o += 1
                        player_x = 0
                if player_x >= self.min_length_deletions or player_o >= self.min_length_deletions:
                    return True
            else:
                player_x, player_o = 0, 0
        return False

    def diagonal_win_to_right(self, board):
        ''' From left to right signs deletions.
        check when we have few same signs in diagonals from middle to top-right corner
        than return True.
        When the input is reversed board function will be checking from middle to bottom-left corner'''
        player_x, player_o = 0, 0
        for loop in range(len(board)):
            for i, arr in enumerate(board):
                if loop + i < len(arr):
                    if arr[loop + i] == 'X' or arr[loop + i] == 'O':
                        if arr[loop + i] == 'X':
                            player_x += 1
                            player_o = 0
                        else:
                            player_o += 1
                            player_x = 0
                    if player_x >= self.min_length_deletions or player_o >= self.min_length_deletions:
                        return True
            else:
                player_x, player_o = 0, 0
        return False

    def diagonal_win_to_left(self, board):
        '''from right to left signs deletions. Similar to diagonal_win_to_right.
        in first we convert board next call above method.
        Convertion example:
        from 
        0 | 1 | 2
        ------------
        3 | 4 | 5
        ------------
        6 | 7 | 8
        to 
        2 | 1 | 0 
        ------------
        5 | 4 | 3 
        ------------
        8 | 7 | 6 
        '''
        reversed_board = [a[::-1] for a in board]
        if self.diagonal_win_to_right(reversed_board):
            return True
        else:
            return False

    def winner(self, board):
        '''check who win. Return True when anybody win.'''
        print(self.printer(board))
        if self.horizontal_win(board) or self.vertical_win(board)\
        or self.diagonal_win_to_right(board)\
        or self.diagonal_win_to_right([a[::-1] for a in board][::-1])\
        or self.diagonal_win_to_left(board) \
        or self.diagonal_win_to_left([a[::-1] for a in board][::-1]):
            print('Win')
            return True
        else:
            print('False')
            return False

    def main(self):
        player = 0
        while True:
            print(self.printer(self.board))
            while True:
                # make sure input value are valid - inputs are digit
                valid_val = self.valid_value()
                if valid_val >= 0:
                    if self.instert_to_board(player, valid_val):
                        if self.winner(self.board):
                            print()
                            return 'WINNER {}'.format('X' if player == 0 else 'O')
                        if self.draw():
                            print()
                            return 'DRAW'
                        break
            # switch between players
            if player == 0:
                player = 1
            else:
                player = 0

def matrix_choice():
    '''determine size of martix necessary to play'''
    while True:
        matrix_choice = input('Please enter size of martix from two to n: ')
        try:
            matrix_choice = int(matrix_choice)
            return matrix_choice
        except:
            print("Dosen't entered number please try again" )

def deletion_condition_to_win(matrix_size):
    '''determine size of deletions signs "X" and "O" in rows, columns or diagonals '''
    while True:
        deletion_choice = input('Please enter number of deletions:'
                                        'Note: 1 <= deletions <= matrix: ')
        try:
            deletion_choice = int(deletion_choice)
            if 1 <= deletion_choice <= matrix_size:
                return deletion_choice
            else:
                print('Error deletions number')
        except:
            print("Dosen't entered number please try again")

def menu():
    print('''\n\n\t"Simple game for two person in Tic Tac Toe.
     Player decides how big the board is. Valid board (2 to n)
     where board are matrix n x n. Good Luck and Have Fun."\n\n''')
    matrix_size = matrix_choice()
    deletion_condition = deletion_condition_to_win(matrix_size)
    return TicTacToe(matrix_size, deletion_condition).main()



if __name__ == '__main__':
    print(menu())