# 我們創建一個Player類別。
from CONSTANTS import CARD
from Card import Card 

class Player: 
    # 我們希望他有名字。
    def __init__(self, name): 
        self.name = name 
        self.hand_cards = [] 

    def reset(self):
        self.__init__(self.name)
    # 我們希望他有 取牌 的功能。
    def getCards(self, cards:list):
        self.hand_cards.extend(cards)
        self.hand_cards.sort()
    # 我們希望他有 出牌 的功能。
    def playCard(self): 
        card = self.strategy()
        return card 
    # 我們希望他有策略，甚麼時候該出甚麼牌。
    # 當然，這裡我們只用最簡單的方式，去實踐它。
    def strategy(self): 
        return self.hand_cards.pop()
    # 用name來表示這個player，而不是記憶體位置。
    def __repr__(self): 
        return self.name

# 我們想要一個聰明的玩家，他可以根據現場情況，判斷自己要出什麼牌。
# 除了出牌的策略和相關方法以外，全部都和普通玩家一樣，所以我們用繼承的方式創建。
class Smart_Player(Player): 
    # 這個聰明的玩家可以把每1回合大家出過的牌記起來。
    # 也可以判斷哪些牌是比較大的牌。
    # 也可以計算自己的大牌，和其他人的大牌。
    def __init__(self, name):
        self.record = [] 
        self.remainingCardOnOthers = [ Card(item[0], item[1]) for item in CARD]
        self.BIG_CARD = [ Card(item[0], item[1]) for item in CARD[-16:] ]
        return super().__init__(name)
    # 每次發牌，都把自己的手牌從52張裡面扣掉，這樣剩下的就是其他人的手牌。
    def getCards(self, cards:list): 
        for card in cards: 
            self.remainingCardOnOthers.remove(card)
        super().getCards(cards)
    # 我們的策略是:
    #   當我手上的大牌比其他人手上的大牌總和還要多的時候，我就從最大的牌開始出，虐殺對方。
    #   但是如果其他人的大牌還很多，那我就從小牌開始出。
    def strategy(self):
        self.updateRemainingCardOnOthers()
        myBigCardAmount = self.calBigCardAmount(self.hand_cards)
        othersBigCardAmount = self.calBigCardAmount(self.remainingCardOnOthers)
        if othersBigCardAmount <= myBigCardAmount : 
            return self.hand_cards.pop() 
        else: 
            return self.hand_cards.pop(0)
    # 更新其他人手上還有甚麼牌。
    def updateRemainingCardOnOthers(self):
        if self.record != []: 
            for i in range(4):  
                card = self.record[-1][i]
                if card in self.remainingCardOnOthers:
                    self.remainingCardOnOthers.remove( card ) 
    # 計算大牌的數量。
    def calBigCardAmount(self, card_list):
        count = 0 
        for card in card_list: 
            if card in self.BIG_CARD: 
                count += 1 
        return count 

