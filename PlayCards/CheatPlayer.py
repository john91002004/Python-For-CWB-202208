from Player import Player
from Card import Card 

class CheatPlayer(Player): 

    def playCard(self): 
        return Card('spade', 'A')