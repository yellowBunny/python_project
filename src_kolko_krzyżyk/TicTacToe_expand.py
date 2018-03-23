
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

    def printer(self):
        '''print board with positions to choose'''
        pattern = ' {}{}|'.format('{}', ' ')
        for i in range(len(self.board)):
            s = ''.join(pattern.format(str(pos).rjust(len(str(self.matrix**2))))
                        for pos in self.board[i]).strip('|')
            print(s)
            if i<len(self.board)-1:
                print('-' * (len(str(self.matrix ** 2)) + 3) * len(self.board[i]))
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
                    else:
                        player_o += 1
                else:
                    player_x, player_o = 0, 0
                if player_x >= self.min_length_deletions or player_o >= self.min_length_deletions:
                    return True

    def vertical_win(self,board):
        '''check when we have few same signs in column than return True'''
        player_x, player_o = 0, 0
        for c in range(len(board)):
            for arr in board :
                if arr[c] == 'X' or arr[c] == 'O':
                    if arr[c] == 'X':
                        player_x += 1
                    else:
                        player_o += 1
                else:
                    player_x, player_o = 0, 0
                if player_x >= self.min_length_deletions or player_o >= self.min_length_deletions:
                    return True

    def diagonal_win(self,board):
        '''check when we have few same signs in diagonals from left to right than return True.
        When the input is reversed board function will be checking from right to left'''
        # print(board)
        player_x, player_o = 0, 0
        for loop in range(len(board)):
            try :
                for i, arr in enumerate(board):
                    print(arr[loop + i])
                    if arr[loop + i] == 'X' or arr[loop + i] == 'O':
                        if arr[i] == 'X':
                            player_x += 1
                        else:
                            player_o += 1
                    else:
                        player_x, player_o = 0, 0
                    if player_x >= self.min_length_deletions or player_o >= self.min_length_deletions:
                        return True
            except:
                return False

    def winner(self, board):
        '''check who win. Return True when anybody win.'''
        if self.horizontal_win(board) or self.vertical_win(board)\
                or self.diagonal_win(board) or self.diagonal_win([a[::-1] for a in board][::-1]):
            return True

    def main(self):
        player = 0
        while True:
            print(self.printer())
            while True:
                # make sure input value are valid - inputs are digit
                valid_val = self.valid_value()
                if valid_val>=0:
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


game = TicTacToe(5)

if __name__ == '__main__':
    print(game.main())