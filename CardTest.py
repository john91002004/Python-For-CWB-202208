import unittest
from Card import Card

class CardTest(unittest.TestCase):

    def testEquality(self): 
        a = Card('spade', 'A')
        b = Card('spade', 'A')
        self.assertEqual(a, b) 

    def testSameSuitComparison(self):
        a = Card('diamond', 2)
        b = Card('diamond', 3)
        self.assertGreater(b, a)

    def testSameValueComparison(self):
        b = Card('diamond', 3)
        c = Card('spade', 3)
        self.assertGreater(c, b)

    


if __name__ == '__main__': 
    unittest.main(verbosity=4)
