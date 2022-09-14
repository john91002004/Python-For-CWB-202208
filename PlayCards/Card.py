from CONSTANTS import CARD

# 我們創建Card類別，讓測試的編譯通過。
class Card: 
    # 我們給定 花色 和 數字 來初始化卡片牌面。
    def __init__(self, suit, value): 
        self.suit = suit 
        self.value = value 
    # 我們讓卡片之間能夠比較 等於
    def __eq__(self, other): 
        return True if self.suit == other.suit and self.value == other.value else False 
    # 我們讓卡片之間能夠比較 大小
    # 寫 __gt__ 和 __eq__ 就等於是把 __lt__ 寫好了
    # 而，我們想要可以用list的index的方式來比較52張牌的方法，於是我們先去把CARD常數寫在CONSTANTS檔案裡，再import進來。
    def __gt__(self, other): 
        a = CARD.index( (self.suit, self.value) )
        b = CARD.index( (other.suit, other.value) )
        return True if a > b else False 
    # 我們發現在測試的輸出當中，我們的Card物件顯示了我不想要看到的記憶體位置，所以我們覆寫這個方法。
    def __repr__(self): 
        return str( (self.suit, self.value) )