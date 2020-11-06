import random
# class to create every card in the deck
class card:
    def __init__(self, number, shape):
        self.number = number
        self.shape = shape

    def show(self):
        return str(self.number) + " of " + self.shape

# class to collect the cards in the deck
class deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):   # a for loop over the shapes and the numbers of values in the deck
        for shape in ["diamond", "red heart", "black heart", "tree"]:
            for num in range(1, 14):
                self.cards.append(card(num, shape))

    def show(self):   # to show the dick
        for card in self.cards:
            card.show()

    def shuffle(self):    # random shuffles the dick
        random.shuffle(self.cards)

    def withdraw(self):   # chooses a card from the dick and delete it
        return self.cards.pop()

class player:  # a class for the people who play the game including the dealer
    def __init__(self, name):
        self.name = name
        self.cards = []  # cards in the hand

    def player_withdraw(self, deck):  # take the paper that was taken from the dick
        self.cards.append(deck.withdraw())

    def show(self):
        if self.name != "Dealer":
            hand = []
            for card in self.cards:
                hand.append(card.show())
            return hand
        else:
            return self.cards[0].show()

    def points(self):
        total = 0
        for card in self.cards:
            if card.number >= 10:
                total += 10
            else:
                total += card.number
        return total

    def new_game(self):
        self.cards = []
