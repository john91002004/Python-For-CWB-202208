import unittest
from Card import Card

# 首先，我們寫一個Test來測試Card必須有的功能:
# 1. 能夠比大小
class CardTest(unittest.TestCase): 

    def testEquality(self): 
        a = Card('spade', 'A')
        b = Card('spade', 'A')
        self.assertEqual(a, b)

    # 我們採用51次的比較，來涵蓋所有的卡片，也就是 黑桃A > 愛心A > 方塊A > 梅花A > ... > 梅花2
    def testComparison(self): 
        SUIT = ['club', 'diamond', 'heart', 'spade']
        VALUE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # 我們比較同數字當中的4種花色，是否符合 黑桃N > 愛心N > 方塊N > 梅花N
        for value in VALUE:
            with self.subTest(Number=value):
                a = Card(SUIT[0], value)
                b = Card(SUIT[1], value)
                c = Card(SUIT[2], value)
                d = Card(SUIT[3], value)
                self.assertGreater(d, c)
                self.assertGreater(c, b)
                self.assertGreater(b, a)
        # 然後，我們比較 梅花3 > 黑桃2  梅花4 > 黑桃3  ...  梅花A > 黑桃K 
        # 這樣，全部就是51次的比較，而這51次比較由數學歸納法得證，可以涵蓋所有的比較組合(52*51/2種組合)
        for i in range(12): 
            a = Card(SUIT[3], VALUE[i])
            b = Card(SUIT[0], VALUE[i+1])
            self.assertGreater(b, a)

if __name__ == '__main__':
    unittest.main(verbosity=4)
