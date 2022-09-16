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
    # 我們測試每1回合後的Winner是不是跟紀錄上寫的相同。
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

    # 我們測試1個賽局的贏家是否和紀錄相同。
    # P.S. 我們在這裡用了跟Game裡面一樣的測試方法，這導致了監守自盜的問題。
    # P.S. 但我們實在是江郎才盡想不出來了，只好出此下策。
    def testMatchWinner(self):
        self.game.runThirteenRounds()
        player_winRound_list = self.recordPlayerWinRound(self.game)
        winner = self.maxWinRoundPlayer(player_winRound_list)
        self.assertEqual(winner, self.game.match_winner)

    def recordPlayerWinRound(self, game):
        winner_list = []
        for round_index in range(13):
            winner_list.append( game.record[round_index][4] ) 
        A_win_round, B_win_round, C_win_round, D_win_round = \
            winner_list.count(self.A), winner_list.count(self.B), winner_list.count(self.C), winner_list.count(self.D)
        return [[self.A, A_win_round], [self.B, B_win_round], [self.C, C_win_round], [self.D, D_win_round]]
        
    def maxWinRoundPlayer(self, ele_list): 
        ele_list = sorted(ele_list, key=lambda s:s[1], reverse=True)
        winner_list = []
        winner_list.append(ele_list[0][0])
        for index in range(1,4):
            if ele_list[index][1] == ele_list[0][1]: 
                winner_list.append(ele_list[index][0])
        return winner_list 


if __name__ == '__main__': 
    unittest.main(verbosity=4)
