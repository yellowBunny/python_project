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
        player_choce = 'dwa'
        instance = TicTacToe_expand.TicTacToe(4)
        self.assertFalse(instance.instert_to_board(player,player_choce))
        d = {12 : [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], ['X', 13, 14, 15]],
             10: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 15]],
             0: [['X', 1, 2, 3], [4, 5, 6, 7], [8, 9, 'X', 11], ['X', 13, 14, 15]]}
        for key,val in d.items():
            self.assertEqual(instance.instert_to_board(player,key),val)


if __name__ == '__main__':
    unittest.main()