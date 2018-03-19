import unittest
import TicTacToe_expand

class TicTacToe_expand_Test(unittest.TestCase):

    def test_prepare_board(self):

        matrix = {3 : [[0,1,2],[3,4,5],[6,7,8]],
                  4 : [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]] }

        for key,val in matrix.items():
            instance = TicTacToe_expand.TicTacToe(key)
            self.assertEqual(instance.prepare_board(key),val)

    def test_used_nums(self):

        matrix = {3 : 3*3 , 4 : 4*4 }
        for key,val in matrix.items():
            print(key,val)
            instance = TicTacToe_expand.TicTacToe(key)
            self.assertEqual(instance.used_nums,['' for loop in range(val)])



if __name__ == '__main__':
    unittest.main()