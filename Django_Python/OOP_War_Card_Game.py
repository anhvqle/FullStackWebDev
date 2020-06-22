# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating A New Deck of Cards")
        self.cards = [(s,r) for s in SUITE for r in RANKS ]
    def __str__(self):
        print(self.cards)
        return  ""
    def shuffle(self):
        shuffle(self.cards)
    def split(self):
        return (self.cards[:26], self.cards[26:])

class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    pass

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass

print("Welcome to War, let's begin...")
deck = Deck()
deck.shuffle()
half1, half2 = deck.split()
print(half1)
print(half2)
