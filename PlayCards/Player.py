# 我們創建一個Player類別。
class Player: 
    # 我們希望他有名字。
    def __init__(self, name): 
        self.name = name 
        self.hand_cards = [] 
    # 我們希望他有 取牌 的功能。
    def getCards(self, cards:list):
        self.hand_cards.extend(cards)
