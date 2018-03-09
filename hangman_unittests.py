import unittest
from hangmnclass import Hangman
class HangmanTest(unittest.TestCase):

    def test_lost(self):
        self.assertEqual(Hangman('ser',3).way_to_lose(),True)
        self.assertEqual(Hangman('ser',2).way_to_lose(),None)
        self.assertEqual(Hangman('kajak',2).way_to_lose(),None)
        self.assertEqual(Hangman('kajak',5).way_to_lose(),True)
        self.assertEqual(Hangman('piesek',6).way_to_lose(),True)

    def test_win(self):
        self.assertEqual(Hangman('ser',0,[ltr for ltr in 'ser']).way_to_win(),True)
        self.assertEqual(Hangman('kajak',0,[ltr for ltr in 'kajak']).way_to_win(),True)
        self.assertEqual(Hangman('kajak',0,['_' for _ in 'kajak']).way_to_win(),False)
        self.assertEqual(Hangman('kajak',0,['_','_','_']).way_to_win(),False)
        self.assertEqual(Hangman('kajak',0,['_','_','j','_','_']).way_to_win(),False)

    def test_board(self):
        self.assertEqual(Hangman('ser',0,['_','_','_']).board('s'), ['s','_','_'])
        self.assertEqual(Hangman('ser',0,['s','_','_']).board('e'), ['s','e','_'])
        self.assertEqual(Hangman('ser',0,['s','e','_']).board('r'), ['s','e','r'])
        self.assertEqual(Hangman('kajak',0,['_','_','_','_','_']).board('k'), ['k','_','_','_','k'])
        self.assertEqual(Hangman('kajak',0,['_','_','_','_','_']).board('j'), ['_','_','j','_','_'])
        self.assertEqual(Hangman('kajak',0,['_','_','_','_','_']).board('a'), ['_','a','_','a','_'])
        self.assertEqual(Hangman('kajak',0,['_','_','j','_','_']).board('a'), ['_','a','j','a','_'])
        self.assertEqual(Hangman('kajak',0,['_','a','j','a','_']).board('k'), ['k','a','j','a','k'])

if __name__ == '__main__':
    unittest.main()