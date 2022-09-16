import random
from CONSTANTS import CARD
from Card import Card

class Game:
    # 我們創建一個賽局，其中必須有4個玩家，才能開賽。
    # 開賽的初始，我們就進行 拿一副新的牌 洗牌 發牌 的動作。
    def __init__(self, A, B, C, D): 
        self.record = [] 
        self.match_winner = [] 
        self.A, self.B, self.C, self.D = A, B, C, D
        self.playerReset()
        self.deck = [ Card(item[0], item[1]) for item in CARD ]  
        self.distributeCards() 
    
    def playerReset(self):
        for player in [self.A, self.B, self.C, self.D]: 
            player.reset()
    # 我們用隨機抽取13張的方式發牌。
    def distributeCards(self):
        for player in [self.A, self.B, self.C, self.D]:
            thirteen_cards = self.randomChooseThirteenCards()
            player.getCards(thirteen_cards)

    def randomChooseThirteenCards(self): 
        indices = random.sample( range(0, len(self.deck)), 13)
        cards = [ self.deck[i] for i in indices ]
        for card in cards: 
            self.deck.remove(card)
        return cards 
    # 每1回合，都做3件事: 叫玩家出牌、比較誰是本回合勝者、將誰出甚麼牌以及勝者記錄起來。
    def round(self): 
        cards = [] 
        for player in [self.A, self.B, self.C, self.D]:
            cards.append( player.playCard() ) 
        winner = self.decideWinner( cards )
        tmp_record = cards.copy()
        tmp_record.append(winner)
        self.record.append( tmp_record )
        for player in [self.A, self.B, self.C, self.D]:
            player.record = self.record.copy()
        
    def decideWinner(self, cards): 
        max_card = max(cards)
        index_max_card = cards.index( max_card )
        return self.correspondingWinner(index_max_card)

    def correspondingWinner(self, index): 
        if index == 0: 
            return self.A
        elif index == 1: 
            return self.B
        elif index == 2: 
            return self.C
        elif index == 3: 
            return self.D
    # 直接跑完1局13回合的比賽，並於遊戲結束時，決定誰是勝者。
    def runThirteenRounds(self):
        for i in range(13):
            self.round()
        self.decideMatchWinner()

    def decideMatchWinner(self): 
        win_round_list = self.recordPlayerWinRound()
        self.match_winner = self.maxWinRoundPlayer(win_round_list)
    # 把每個玩家和他的勝場數，存成一個list。
    def recordPlayerWinRound(self):
        winner_list = []
        for round_index in range(13):
            winner_list.append( self.record[round_index][4] ) 
        A_win_round, B_win_round, C_win_round, D_win_round = \
            winner_list.count(self.A), winner_list.count(self.B), winner_list.count(self.C), winner_list.count(self.D)
        return [[self.A, A_win_round], [self.B, B_win_round], [self.C, C_win_round], [self.D, D_win_round]]
    # 從list裡面挑選出勝出最多場的玩家。
    # 可能不只一個，所以會是一個list。
    def maxWinRoundPlayer(self, ele_list): 
        ele_list = sorted(ele_list, key=lambda s:s[1], reverse=True)
        winner_list = []
        winner_list.append(ele_list[0][0])
        for index in range(1,4):
            if ele_list[index][1] == ele_list[0][1]: 
                winner_list.append(ele_list[index][0])
        return winner_list 
