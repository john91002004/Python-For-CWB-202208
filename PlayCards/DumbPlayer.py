from Player import Player


class DumbPlayer(Player): 

    def strategy(self):
        return max(self.hand_cards)