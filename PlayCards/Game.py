import random
from CONSTANTS import CARD
from Card import Card

class Game:
    # 我們創建一個賽局，其中必須有4個玩家，才能開賽。
    # 開賽的初始，我們就進行 拿一副新的牌 洗牌 發牌 的動作。
    def __init__(self, A, B, C, D): 
        self.initializePlayers(A, B, C, D) 
        self.initializeVariable()
        self.playerReset()
        self.distributeCards() 
    
    def initializePlayers(self, A, B, C, D):
        self.__players = [A, B, C, D]

    def initializeVariable(self):
        self.record = [] 
        self.card_on_player = []
        self.match_winner = [] 
        self.deck = [ Card(item[0], item[1]) for item in CARD ]  

    def playerReset(self):
        for player in self.__players: 
            player.reset()
    # 我們用隨機抽取13張的方式發牌，並記錄起來。
    def distributeCards(self):
        for player in self.__players:
            thirteen_cards = self.randomChooseThirteenCards()
            player.getCards(thirteen_cards)
            self.card_on_player.append(thirteen_cards)

    def randomChooseThirteenCards(self): 
        indices = random.sample( range(0, len(self.deck)), 13)
        cards = [ self.deck[i] for i in indices ]
        for card in cards: 
            self.deck.remove(card)
        return cards 

    # 每1回合，都做3件事: 叫玩家出牌、比較誰是本回合勝者、將誰出甚麼牌以及勝者記錄起來。
    # P.S. 我們再加1件事: 必須有裁判檢查是否有人出千。
    def round(self): 
        thisRoundCards = self.callPlayerToPlayCard()
        self.checkIfPlayerCheat(thisRoundCards)
        self.updateCardOnPlayer(thisRoundCards) 
        winner = self.decideRoundWinner( thisRoundCards )
        self.recordThisRoundToRecord(thisRoundCards, winner)
        self.updateRecordForPlayers()
        
    def callPlayerToPlayCard(self): 
        cards = [] 
        for player in self.__players:
            cards.append( player.playCard() ) 
        return cards 

    def checkIfPlayerCheat(self, cards): 
        for i in range(4):
            if cards[i] not in self.card_on_player[i]:
                raise Exception(f'{self.__players[i]} is cheating, he/she does not have the card {cards[i]}.') 

    def updateCardOnPlayer(self, cards): 
        for i in range(4): 
            self.card_on_player[i].remove(cards[i])

    def decideRoundWinner(self, cards): 
        max_card = max(cards)
        index_max_card = cards.index( max_card )
        return self.correspondingWinner(index_max_card)

    def correspondingWinner(self, index): 
        return self.__players[index]

    def recordThisRoundToRecord(self, thisRoundCards:list, winner):
        tmp_record = thisRoundCards.copy()
        tmp_record.append(winner)
        self.record.append( tmp_record )

    def updateRecordForPlayers(self): 
        for player in self.__players:
            player.record = self.record.copy()
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
        win_round = [] 
        for i in range(4): 
            win_round.append( winner_list.count( self.__players[i] ) ) 
        return [ [self.__players[i], win_round[i]] for i in range(4) ] 
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
