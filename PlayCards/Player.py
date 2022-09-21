# 我們創建一個Player類別。
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
    # 我們希望他有 出牌 的功能。
    def playCard(self): 
        card = self.strategy()
        self.hand_cards.pop( self.hand_cards.index(card) ) 
        return card 
    # 我們希望他有策略，甚麼時候該出甚麼牌。
    # 當然，這裡我們只用最簡單的方式，去實踐它。
    def strategy(self): 
        return self.hand_cards[-1]
    # 用name來表示這個player，而不是記憶體位置。
    def __repr__(self): 
        return self.name

