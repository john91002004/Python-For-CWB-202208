class Card:

    def __init__(self, suit, value):
        self.suit = suit 
        self.value = value 

    def __repr__(self): 
        return str( (self.suit, self.value) )

    def __eq__(self, other):
        return True if self.suit == other.suit and self.value == other.value else False 

    def __gt__(self, other):
        if self.value > other.value:
            return True 
        elif self.value < other.value:
            return False 
        else: 
            if self.suit > other.suit: 
                return True 
            else: 
                return False 
