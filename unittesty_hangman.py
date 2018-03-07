import unittest
from zabawa import next_prime
from random import choice

class TestCodewats(unittest.TestCase):
    def test_next_prime(self):
        d = {10: 11, 12: 13, 100: 101, 12312412: 12312413, 2: 3}
        for key in d:
            print(key,d)
            self.assertEqual(next_prime(key),d[key])

    def test_random_next_prime(self):
        r = [choice(list(range(2,10000))) for loop in range(10000)]
        random_key = {key:next_prime(key) for key in r}
        for key in random_key:
            print(key,random_key[key])
            self.assertEqual(next_prime(key),random_key[key])

if __name__ == '__main__':
    unittest.main()