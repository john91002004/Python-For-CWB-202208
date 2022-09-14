import unittest
from Player import Player
# 拿牌
# 用腦子玩牌，決定怎麼出
# 出牌

# 在寫好CardTest和Card以後，我們寫了一個PlayerTest。
class PlayerTest(unittest.TestCase):
    # 我們希望這一個Player有 取牌 的功能。
    # 取牌前應該沒有手牌，取牌後應該有相對應數量的手牌。
    # 並且，有相對應的牌。
    def testGetCards(self): 
        a = Player("John") 
        cards = [('spade', '2'), ('diamond', 'K')]
        self.assertEqual( len(a.hand_cards), 0) 

        a.getCards(cards) 
        self.assertEqual( len(a.hand_cards), 2) 
        
        for card in cards:
            with self.subTest(card=card):
                self.assertIn(card, a.hand_cards)
        

if __name__ == '__main__':
    unittest.main(verbosity=4)
