class TicTacToe:
    #class veribles
    used_nums = []
    board = []
    way_to_win = []

    def __init__(self,martix):
        self.board = [[str(n) for n in range(martix)]for arr in range(martix)]
        self.used_nums = ['' for n in range(martix*martix)]
        self.way_to_win = self.way_to_win

    # def printer(self):
    #     'print board with positions to choose'
    #     print('{}\n{}\n{}'.format(self.board[0], self.board[1], self.board[2]))

    def instert_to_board(self, player, player_choice):
        '''inserting player to board return update board '''
        counter = 0
        for arr in self.board:
            for i, pos in enumerate(arr):
                if player_choice == counter:
                    arr[i] = 'X' if player == 0 else 'O'
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



game = TicTacToe(3)

# if __name__ == '__main__':
#     game.main_func()
