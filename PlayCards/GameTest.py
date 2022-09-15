import unittest
from Game import Game
from Player import Player

# 我們希望Game有什麼功能，就先把Test寫出來，同時也逼迫我們思考我們的Game要長成怎麼樣。
class GameTest(unittest.TestCase):
    # 首先創建一個Game物件，必須有4個玩家，作為初始化的參數。
    def setUp(self) -> None:
        self.A, self.B, self.C, self.D = Player('John'), Player('Jenny'), Player('Jordan'), Player('Jan')
        self.game = Game(self.A, self.B, self.C, self.D) 
        return super().setUp()
    # 我們測試是不是在發牌完之後，每個人都有13張牌。
    def testEveryPlayerGotThirteenCardsAfterDistribution(self): 
        for player in [self.A, self.B, self.C, self.D]: 
            with self.subTest(player=player):
                self.assertEqual( len(player.hand_cards), 13 )
    # 我們測試第1回合結束之後，每一個人應該要剩下12張牌。
    def testRemainingCardsAfterOneRound(self): 
        self.game.round()
        for player in [self.A, self.B, self.C, self.D]: 
            with self.subTest(player=player):
                self.assertEqual( len(player.hand_cards), 12 )
    # 我們測試在每1回合結束之後，每一個人的牌的數量。
    def testRemainingCardsAfterEachRound(self): 
        for count in range(1,14):
            self.game.round()
            for player in [self.A, self.B, self.C, self.D]: 
                with self.subTest(round=count, player=player):
                    self.assertEqual( len(player.hand_cards), 13-count )
    # 我們測試第1回合後的Winner是不是跟紀錄上寫的相同。
    # P.S. 由於隨機的關係，我們沒有辦法確定每一回合的勝者，以及誰出了甚麼牌，
    # P.S. 所以我們只能暫且將record上，每一個人出的牌當作是正確的，並以此作為依據判斷誰是勝者，
    # P.S. 再將我們的勝者和紀錄上的勝者做比較，並斷言其相同。
    def testWinnerAfterOneRound(self): 
        self.game.round() 
        cardsPlayed = self.game.record[0][0:4]
        record_winner = self.game.record[0][4]
        winner_index = cardsPlayed.index( max(cardsPlayed) )
        winner = self.correspondingWinner(winner_index)
        self.assertEqual(record_winner, winner)

    def testWinnerAfterEachRound(self): 
        for count in range(1,14): 
            with self.subTest(round=count):
                self.game.round() 
                cardsPlayed = self.game.record[count-1][0:4]
                record_winner = self.game.record[count-1][4]
                winner_index = cardsPlayed.index( max(cardsPlayed) )
                winner = self.correspondingWinner(winner_index)
                self.assertEqual(record_winner, winner)

    def correspondingWinner(self, index): 
        if index == 0: 
            return self.A
        elif index == 1: 
            return self.B
        elif index == 2: 
            return self.C
        elif index == 3: 
            return self.D


if __name__ == '__main__': 
    unittest.main(verbosity=4)
