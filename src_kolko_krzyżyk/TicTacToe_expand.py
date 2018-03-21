
class TicTacToe:

    def __init__(self,martix):
        self.matrix = martix
        self.board = self.prepare_board()
        self.used_nums = ['' for _ in range(martix*martix)]
        self.way_to_win = []

    def printer(self):
        '''print board with positions to choose'''
        pattern = ' {}{}|'.format('{}', ' ')
        for i in range(len(self.board)):
            s = ''.join(pattern.format(str(pos).rjust(len(str(self.matrix**2))))
                        for pos in self.board[i]).strip('|')
            print(s)
            if i<len(self.board)-1:
                print('-'*(len(str(self.matrix**2))+3)*len(self.board[i]))
        return ''

    def prepare_board(self):
        '''preparing a board to play - matrix board'''
        if type(self.matrix)!= int:
            raise ValueError
        board = []
        start = 0
        next_numbers = self.matrix
        for arr in range(self.matrix):
            board+=[[i for i in range(start, next_numbers)]]
            start+=self.matrix
            next_numbers+=self.matrix
        return board

    def instert_to_board(self, player, player_choice):
        '''inserting player to board return update board '''
        while True:
            # check if variable are digit
            try:
                player_choice = int(player_choice)
                break
            except:
                print('only numbers please')
                return False

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
                      (player_choice, len(self.used_nums)-1))

    def draw(self):
        'when all fild are occupied in used_nums return True'
        return all(1 if ele != '' else 0 for ele in self.used_nums)



    # def winner(self):
    #     '''check who win. Return True when anybody win.'''
    #     for arr in self.way_to_win:
    #         if (0 == self.used_nums[arr[0]] == self.used_nums[arr[1]] == self.used_nums[arr[2]] or
    #             1 == self.used_nums[arr[0]] == self.used_nums[arr[1]] == self.used_nums[arr[2]]):
    #             return True



    def main(self):
        player = 0
        print(self.board)
        while True:
            print(self.printer())
            while True:
                choice = input('Choose field 0-{}: '.format(len(self.used_nums) - 1))
                if self.instert_to_board(player, choice):
                    if self.draw():
                        print()
                        return 'DRAW'
                    break
            # switch between players
            if player == 0:
                player = 1
            else:
                player = 0

game = TicTacToe(4)

if __name__ == '__main__':
    print(game.main())