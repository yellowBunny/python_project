import unittest
import TicTacToe_expand

class TicTacToe_expand_Test(unittest.TestCase):

    def test_prepare_board(self):
        '''test valid numbers of columns and rows in matrix'''

        matrix = {3 : [[0,1,2],[3,4,5],[6,7,8]],
                  4 : [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]] }

        for key, val in matrix.items():
            instance = TicTacToe_expand.TicTacToe(key)
            self.assertEqual(instance.prepare_board(),val)

    def test_used_nums(self):
        '''make sure we have correct list with empty fields'''

        matrix = {3 : 3*3 , 4 : 4*4 }

        for key,val in matrix.items():
            print(key,val)
            instance = TicTacToe_expand.TicTacToe(key)
            self.assertEqual(instance.used_nums,['' for _ in range(val)])

    def test_insert_to_board(self):
        '''make sure we have valid value in valid fields '''
        player = 0
        instance = TicTacToe_expand.TicTacToe(4)
        self.assertEqual(instance.instert_to_board(player,12),
                         [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], ['X', 13, 14, 15]])
        self.assertEqual(instance.instert_to_board(player, 10),
                         [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 15]])
        self.assertEqual(instance.instert_to_board(player, 0),
                         [['X', 1, 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 15]])
        player = 1
        self.assertEqual(instance.instert_to_board(player, 1),
                         [['X', 'O', 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 15]])
        self.assertEqual(instance.instert_to_board(player, 15),
                         [['X', 'O', 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 'O']])

    def test_horizontal_win(self):
        '''make sure we have few same signs in row'''

        # board with examples where func should return True
        instance = TicTacToe_expand.TicTacToe(4)
        boards = [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'X', 'O'], ['X', 'X', 'X', 'O']],
                [[0, 1, 2, 3], [4, 'X', 'X', 'X'], [8, 9, 'X', 11], ['X', 13, 14, 'O']],
                [[0, 1, 2, 3], [4, 5, 6, 'X'], ['X', 'X', 'X', 11], ['X', 13, 14, 'O']],]

        for arr in boards:
            self.assertTrue(instance.horizontal_win(arr))

        # board with examples where func should return False
        boards = [[['X', 1, 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 'O']],
                  [['X', 1, 'X', 3], [4, 5, 'O', 7], [8, 9, 'X', 11], ['X', 13, 14, 'O']],
                  [['X', 1, 'X', 3], ['X', 5, 'O', 7], ['O', 9, 'X', 11], ['X', 13, 14, 'O']],
                  [[0, 1, 'X', 'X'], ['X', 5, 'O', 7], ['O', 9, 'X', 11], ['X', 13, 14, 'O']],
                  [[0, 1, 2, 3], ['O', 'O', 'X', 'O'], ['O', 'O', 10, 11], ['O', 13, 14, 'O']],
                  [[0, 1, 'O', 'O'], ['O', 5, 6, 7], [8, 9, 10, 11], ['O', 13, 14, 'O']],
                  [[0, 1, 'X', 'X'], ['X', 5, 6, 7], [8, 9, 10, 11], ['O', 13, 14, 'O']],]

        for arr in boards:
            self.assertFalse(instance.horizontal_win(arr))

    def test_vertical_win(self):
        '''make sure we have few same signs in column'''

        # board with examples where func should return True
        instance = TicTacToe_expand.TicTacToe(4)
        boards = [[['X', 1, 2, 3], ['X', 5, 6, 7], ['X', 9, 10, 11], [12, 13, 14, 15]],
                  [[0, 1, 2, 'O'], ['X', 5, 'O', 7], ['X', 9, 'O', 11], ['X', 13, 14, 15]],
                  [[0, 'X', 2, 3], [4, 5, 'O', 7], [8, 9, 'O', 11], [12, 13, 'O', 15]],
                  [['X', 1, 2, 3], ['X', 5, 6, 'O'], [8, 9, 10, 'O'], [12, 13, 14, 'O']]]

        for arr in boards:
            self.assertTrue(instance.vertical_win(arr))

        # board with examples where func should return False

        boards = [[['X', 1, 2, 3], ['O', 5, 6, 7], ['X', 9, 10, 11], [12, 13, 14, 15]],
                  [[0, 1, 2, 'O'], ['O', 5, 'O', 7], ['X', 9, 'O', 11], ['X', 13, 14, 15]],
                  [[0, 'X', 2, 3], [4, 5, 'O', 7], [8, 9, 'X', 11], [12, 13, 'O', 15]]]

        for arr in boards:
            self.assertFalse(instance.vertical_win(arr))

    def test_diagonal_win(self):
        '''make sure we have few same signs in diagonals'''
        instance = TicTacToe_expand.TicTacToe(4)

        #board with examples where func should return True 4 x 4

        boards = [[['X', 1, 'O', 3],[4, 'X', 6, 7],[8, 9, 'X', 11],[12, 'O', 14, 15]],
                  [[0, 'X', 2, 'X'], [4, 5, 'X', 7], [8, 'O', 10, 'X'], [12, 13, 14, 15]],
                  [[0, 'O', 'X', 3], ['X', 5, 6, 7], [8, 'X', 10, 11], [12, 13, 'X', 15]],
                  [[0, 1, 2, 3], [4, 'O', 6, 7], [8, 7, 'O', 11], [12, 13, 14, 'O']],
                  [[0, 1, 'X', 3], [4, 'O', 6, 7], [8, 7, 'O', 'X'], [12, 'O', 14, 'O']]]

        for i, arr in enumerate(boards):
            # checking from left to right
            if i < 2:
                self.assertTrue(instance.diagonal_win(arr))
            #checking form right to left
            else:
                print([a[::-1] for a in arr][::-1])
                self.assertTrue(instance.diagonal_win([a[::-1] for a in arr][::-1]))

        # board with examples where func should return False
        boards = [[[0, 1, 'X', 3], [4, 5, 6, 'X'], [8, 9, 10, 11], ['X', 13, 14, 15]],
                  [['X', 1, 'O', 3], ['X', 5, 6, 'X'], ['O', 'O', 10, 11], ['X', 13, 14, 15]],]

        for arr in boards:
            self.assertFalse(instance.diagonal_win(arr))

        # board with examples where func should return True
        instance = TicTacToe_expand.TicTacToe(5)

        boards = [[[0, 1, 'X', 3, 4], [5, 6, 7, 'X', 9], [10, 11, 12, 13, 'X'],
            [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]],
             [['O', 1, 'X', 3, 4], [5, 'O', 7, 'X', 9], [10, 11, 'O', 13, 'X'],
            [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]],]

        for arr in boards:
            self.assertTrue(instance.diagonal_win(arr))

        # reversed test
        boards = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 'X', 13, 14],
         [15, 16, 17, 'X', 19], [20, 21, 22, 23, 'X']]

        self.assertTrue(instance.diagonal_win([a[::-1] for a in boards][::-1]))


    def test_winner(self):
        instance = TicTacToe_expand.TicTacToe(4)
        boards = [[['X', 1, 'O', 3], [4, 'X', 6, 7], [8, 9, 'X', 11], [12, 'O', 14, 15]],
                  [[0, 'X', 2, 'X'], [4, 5, 'X', 7], [8, 'O', 10, 'X'], [12, 13, 14, 15]],
                  [[0, 'O', 'X', 3], ['X', 5, 6, 7], [8, 'X', 10, 11], [12, 13, 'X', 15]],
                  [['X', 1, 2, 3], ['X', 5, 6, 7], ['X', 9, 10, 11], [12, 13, 14, 15]],
                  [[0, 1, 2, 'O'], ['X', 5, 'O', 7], ['X', 9, 'O', 11], ['X', 13, 14, 15]],
                  [[0, 'X', 2, 3], [4, 5, 'O', 7], [8, 9, 'O', 11], [12, 13, 'O', 15]],
                  [['X', 1, 2, 3], ['X', 5, 6, 'O'], [8, 9, 10, 'O'], [12, 13, 14, 'O']],
                  [[0, 1, 2, 3], [4, 'O', 6, 7], [8, 7, 'O', 11], [12, 13, 14, 'O']],]

        for arr in boards:
            self.assertTrue(instance.winner(arr))



if __name__ == '__main__':
    unittest.main()