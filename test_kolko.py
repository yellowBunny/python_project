import unittest
import kolko_pve
import random
sign = ['X','O','']
l = [[random.choice(sign) for lenght in range(9)] for arrays in range(100)]
ll = [arr for arr in l if not all([ele for ele in arr])]
dd = {tuple(key):[0,1,2,3,4,5,6,7,8] for key in ll}
print(dd)

class TestKolko(unittest.TestCase):

    def test_AI_moves(self):
        d = {4:['','','','','','','','',''],0:['', '', '', '', 'X', '', '', '', ''],2:['X', 'X', '', '', '', '', '', '', ''],
             6:['X', 'O', 'X', 'X', '', 'O', '', 'X', 'O']}
        for key in d:
            self.assertEqual(kolko_pve.AI_moves(d[key]),key)

    def test_AI_moves_random(self):
        for key in dd:
            self.assertIn(kolko_pve.AI_moves(key),dd[key])

    def test_draw(self):
        self.assertTrue(kolko_pve.draw(['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']))
        self.assertFalse(kolko_pve.draw(['', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O']))
        self.assertFalse(kolko_pve.draw(['', '', '', '', '', '', '', '', '']))

    def test_winner(self):
        self.assertTrue(kolko_pve.winner(['X', 'X', 'X', 'O', 'X', 'O', 'X', 'X', 'O']))
        self.assertTrue(kolko_pve.winner(['X', 'X', '', 'O', 'X', 'O', 'X', 'X', 'O']))
        self.assertFalse(kolko_pve.winner(['', '', '', '', '', '', '', '', '']))
        self.assertFalse(kolko_pve.winner(['X', 'X', '', 'O', 'X', 'O', 'X', 'O', 'O']))

    # def test_human(self):
    #     self.assertEqual(kolko_pve.human(1),1)
    #     self.assertEqual(kolko_pve.human(8), 8)

    def test_insert_to_tab(self):
        pass


if __name__ == '__main__':

    unittest.main()