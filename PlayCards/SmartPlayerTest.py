import unittest
from Card import Card
from SmartPlayer import Smart_Player

class SmartPlayerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.a = Smart_Player("John") 
        self.cards = [Card('spade', '2'), Card('diamond', 'K')]
        return super().setUp()

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
        
    def testPlayerReset(self): 
        self.a.reset()
        self.assertEqual(self.a.hand_cards, [])

if __name__ == '__main__':
    unittest.main(verbosity=4)