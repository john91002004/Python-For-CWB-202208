from CONSTANTS import CARD
from Card import Card
from MathFunction import calCombinationAmount
from Player import Player
# 我們想要一個聰明的玩家，他可以根據現場情況，判斷自己要出什麼牌。
# 除了出牌的策略和相關方法以外，全部都和普通玩家一樣，所以我們用繼承的方式創建。
class Smart_Player(Player): 
    # 這個聰明的玩家可以把每1回合大家出過的牌記起來。
    # 也可以判斷哪些牌是比較大的牌。
    # 也可以計算自己的大牌，和其他人的大牌。
    def __init__(self, name, prob):
        self.prob = prob
        self.record = [] 
        self.remainingCardOnOthers = [ Card(item[0], item[1]) for item in CARD]
        self.BIG_CARD = [ Card(item[0], item[1]) for item in CARD[-16:] ]
        return super().__init__(name)
    
    def reset(self):
        self.__init__(self.name, self.prob)
    # 每次發牌，都把自己的手牌從52張裡面扣掉，這樣剩下的就是其他人的手牌。
    def getCards(self, cards:list): 
        for card in cards: 
            self.remainingCardOnOthers.remove(card)
        super().getCards(cards)
        self.hand_cards.sort(reverse=True)
    # 我們的策略是:
    #   計算出我們手牌上，勝率大於 50%(預設) 的牌有幾張。
    #    - 如果有超過1張，就取其中最小的出牌。
    #    - 如果沒有牌，就取整個手牌中最小的牌。
    def strategy(self):
        self.updateRemainingCardOnOthers()
        card = self.calMinimumCardMeetWinRate(self.prob)
        return card 
    # 更新其他人手上還有甚麼牌。
    def updateRemainingCardOnOthers(self):
        if self.record != []: 
            for i in range(4):  
                card = self.record[-1][i]
                if card in self.remainingCardOnOthers:
                    self.remainingCardOnOthers.remove( card ) 
    # 計算每一張手牌的勝率。
    def calMinimumCardMeetWinRate(self, probability=0.5):
        card_index = 0 
        for card in self.hand_cards: 
            if self.calWinRate(card) >= probability: 
                card_index += 1 
            else: 
                break 
        card_index -= 1 
        return self.hand_cards[card_index]
    
    def calWinRate(self, card): 
        other_bigger_card_amount = self.calOtherCardAmountBiggerThan(card)
        other_remain_card_amount = len( self.remainingCardOnOthers )
        total_combination = calCombinationAmount( other_remain_card_amount, 3)
        win_combination = calCombinationAmount( other_remain_card_amount - other_bigger_card_amount, 3)
        return win_combination / total_combination
    
    def calOtherCardAmountBiggerThan(self, card):
        count = 0 
        for other_card in self.remainingCardOnOthers: 
            if other_card > card: 
                count += 1 
        return count 

