# Rules: https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class.You can then use this Deck list of cards to split in
    half and give to the players. It should also have a method for splitting/cutting
    the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = [(r,s) for s in SUITE for r in RANKS ]

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
    cards from that hand.
    '''
    def __init__(self, cards):
        self.cards = cards          #cards is a list of tuples

    def add(self, card):
        self.cards.insert(0, card)

    def remove(self):
        return self.cards.pop()

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, name, Hand):
        self.name = name
        self.Hand = Hand

    def play_card(self):
        drawn_card = self.Hand.remove()
        print("{} played: {}".format(self.name, drawn_card))
        return drawn_card

    def still_has_cards(self):
        return len(self.Hand.cards) != 0

    def __str__(self):
        return self.name


print("Welcome to War, let's begin...")
deck = Deck()
deck.shuffle()
half1, half2 = deck.split()

userName = input("What is your name? ")
print()
computer = Player("Computer", Hand(half1))          #Computer takes 1st half of the Deck
user = Player(userName, Hand(half2))                #User takes 2nd half of the Deck
i = 0
while user.still_has_cards() and computer.still_has_cards():
    print('\n')
    print("Here are the current standings: ")
    print(user.name+"'s count: " + str(len(user.Hand.cards)))
    print(computer.name+"'s count: " + str(len(computer.Hand.cards)))
    print()

    print(computer.name, ":", half1, '\n')
    print(user.name, ":",  half2, '\n')

    print("Both players play a card!\n")

    #Cards being played represented by a list
    playedCards = []
    userCard = user.play_card()
    compCard = computer.play_card()
    playedCards.append(userCard)
    playedCards.append(compCard)

    if(userCard[0] == compCard[0]):
        print("------------------------------There is a match. Time for War!------------------------------")
        print("Each player removes 3 cards 'face down' and then one card face up")

        if(len(user.Hand.cards) >= 3 and len(computer.Hand.cards) >= 3):
            for x in range(3):
                playedCards.append(user.Hand.cards.pop())
                playedCards.append(computer.Hand.cards.pop())
        else:
            playedCards.extend(user.Hand.cards)
            playedCards.extend(computer.Hand.cards)

        userCard = user.play_card()
        compCard = computer.play_card()
        playedCards.append(userCard)
        playedCards.append(compCard)
        if(RANKS.index(userCard[0]) > RANKS.index(compCard[0])):
            print(user.name+" has the higher card, adding to hand.")
            for card in playedCards:
                user.Hand.add(card)
        else:
            print(computer.name+" has the higher card, adding to hand.")
            for card in playedCards:
                computer.Hand.add(card)

    else:
        if(RANKS.index(userCard[0]) > RANKS.index(compCard[0])):
            print(user.name+" has the higher card, adding to hand.")
            for card in playedCards:
                user.Hand.add(card)
        else:
            print(computer.name+" has the higher card, adding to hand.")
            for card in playedCards:
                computer.Hand.add(card)

print('\n')
if(len(user.Hand.cards) > len(computer.Hand.cards)):
    print("GAME OVER!", userName.upper(), "WINS !")
else:
    print("GAME OVER. COMPUTER WINS !")
