
class TicTacToe:

    def __init__(self,martix):
        self.matrix = martix
        self.board = self.prepare_board()
        self.used_nums = ['' for _ in range(martix*martix)]
        self.way_to_win = []

    def printer(self):
        '''print board with positions to choose'''
        pattern = ' {}{}|'.format('{}',' ')
        for i in range(len(self.board)):
            s = ''.join(pattern.format(str(pos).rjust(len(str(self.matrix**2))))
                        for pos in self.board[i]).strip('|')
            print(s)
            if i<len(self.board)-1:
                print('-'*(len(str(self.matrix**2))+3)*len(self.board[i]))

    def prepare_board(self):
        '''preparing a board to play - matrix board'''
        if type(self.matrix)!= int:
            raise ValueError
        board = []
        start = 0
        next_numbers = self.matrix
        for arr in range(self.matrix):
            board+=[[i for i in range(start,next_numbers)]]
            start+=self.matrix
            next_numbers+=self.matrix
        return board

    def instert_to_board(self, player, player_choice):
        '''inserting player to board return update board '''
        if type(player_choice)!=int:
            raise ValueError
        counter = 0
        for arr in self.board:
            for i in range(len(arr)):
                if player_choice == counter:
                    arr[i] = 'X' if player == 0 else 'O'
                    self.used_nums[counter] = player
                counter += 1
        return self.board

    # def winner(self):
    #     '''check who win. Return True when anybody win.'''
    #     for arr in self.way_to_win:
    #         if (0 == self.used_nums[arr[0]] == self.used_nums[arr[1]] == self.used_nums[arr[2]] or
    #             1 == self.used_nums[arr[0]] == self.used_nums[arr[1]] == self.used_nums[arr[2]]):
    #             return True

    def draw(self):
        'when all fild are occupied in used_nums return True'
        return all(1 if ele != '' else 0 for ele in self.used_nums)


    def main_func(self):
        'main function'
        print(self.instert_to_board(0,15))
        print(self.instert_to_board(1,0))
        print(self.instert_to_board(0,4))
        print(self.used_nums)
        print(self.printer())


game = TicTacToe(20)

if __name__ == '__main__':
    game.main_func()