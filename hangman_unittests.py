import unittest
from hang_man import HangMan
class HangmanTest(unittest.TestCase):


    def test_win_lost(self):
        p1 = HangMan('ser')
        self.assertEqual(HangMan.win_lost(p1,['a', 'a', 'c']),True)
        self.assertEqual(HangMan.win_lost(p1,['_','b''_']),False)
        self.assertEqual(HangMan.win_lost(p1,['1','1','1']),False)
        self.assertEqual(HangMan.win_lost(p1,['','','']),False)

    def test_words(self):
        p1 = HangMan(['_','_','_'])
        self.assertEqual(HangMan.words(p1,'s'), ['s','_','_'])
        # self.assertEqual(HangMan.words(p1,'e'), [1])
        # self.assertEqual(HangMan.words(p1,'r'), [2])
        # p2 = HangMan('kajak')
        # self.assertEqual(HangMan.words(p2,'k'), [0,4])
        # p3 = HangMan('wiweraw')
        # self.assertEqual(HangMan.words(p3, 'w'), [0,2,6])


if __name__ == '__main__':
    unittest.main()