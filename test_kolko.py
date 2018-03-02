import unittest
import kolko_pve
import random

sign = ['X','O','']
l = [[random.choice(sign) for lenght in range(9)] for arrays in range(100)]

class TestKolko(unittest.TestCase):

    def test_AI_moves(self):
        dd = {4:['','','','','','','','',''],0:['', '', '', '', 'X', '', '', '', ''],2:['X', 'X', '', '', '', '', '', '', ''],
             6:['X', 'O', 'X', 'X', '', 'O', '', 'X', 'O'], 7:['', 'O', 'X', 'X', 'O', 'X', '', '', 'O']}
        for key in dd:
            self.assertEqual(kolko_pve.AI_moves(dd[key]),key)

    def test_AI_moves_random(self):

        way_to_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        best_moves = [4, 0, 8, 2, 6, 7, 3, 1, 5]

        d = {tuple(key):[] for key in l if not all(pos for pos in key)}


        def win_in_row(tab, sign):
            for arr in way_to_win:
                if sum(1 for pos in arr if tab[pos] == '{}'.format(sign)) >= 2:
                    choice = [pos for pos in arr if not tab[pos]]
                    if choice:
                        return '0' if choice[-1]==0 else choice[-1]
        for arr in l:
            x = win_in_row(arr, 'X')
            o = win_in_row(arr, 'O')
            for i in best_moves:
                if not arr[i]:
                    d[tuple(arr)] = [i]
                    if x:
                        d[tuple(arr)] += [int(x)]
                    if o:
                        d[tuple(arr)] += [int(o)]
                    break

        for key in d:
            self.assertIn(kolko_pve.AI_moves(key),d[key])


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