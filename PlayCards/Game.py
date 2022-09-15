
# 跑13回合
import random
from CONSTANTS import CARD
from Card import Card


class Game:
    # 我們創建一個賽局，其中必須有4個玩家，才能開賽。
    # 開賽的初始，我們就進行 拿一副新的牌 洗牌 發牌 的動作。
    def __init__(self, A, B, C, D): 
        self.record = [] 
        self.A, self.B, self.C, self.D = A, B, C, D
        self.deck = [ Card(item[0], item[1]) for item in CARD ]  
        self.distributeCards() 
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

