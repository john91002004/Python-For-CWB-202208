import unittest
from Card import Card
from Player import Player

# 在寫好CardTest和Card以後，我們寫了一個PlayerTest。
class PlayerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.a = Player("John") 
        self.cards = [Card('spade', '2'), Card('diamond', 'K')]
        return super().setUp()
    # 我們希望這一個Player有 取牌 的功能。
    # 取牌前應該沒有手牌，取牌後應該有相對應數量的手牌。
    # 並且，有相對應的牌。
    def testGetCards(self): 
        self.assertEqual( len(self.a.hand_cards), 0) 

        self.a.getCards(self.cards) 
        self.assertEqual( len(self.a.hand_cards), 2) 
        
        for card in self.cards:
            with self.subTest(card=card):
                self.assertIn(card, self.a.hand_cards)
    
    def testPlayCards(self): 
        self.a.getCards(self.cards)
        tmp = []
        tmp.append( self.a.playCard() )
        tmp.append( self.a.playCard() )
        self.assertIn(tmp[0], self.cards)
        self.assertIn(tmp[1], self.cards)
    # 在Player Reset之後，手牌應該要是空的。
    def testPlayerReset(self): 
        self.a.reset()
        self.assertEqual(self.a.hand_cards, [])

if __name__ == '__main__':
    unittest.main(verbosity=4)
