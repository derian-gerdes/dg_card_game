"""
File: cards.py

Module for playing cards, with classes Card and Deck
""" 
import random

class Card(object):
    """ A card object with a suit and rank."""
    
    Names = ('2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace')
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('s', 'd', 'h', 'c')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit
        self.name = self.Names[self.rank-1]
        self.imgname = 'DECK/' + str(self.rank) + suit + '.gif'
        
    def __str__(self):
        """Returns the string representation of a card."""
        return self.name + ' of ' + self.suit
    def getImg(self):
        return self.imgname;

    def __gt__(self, other):
        return self.rank > other.rank
    def __eq__(self, other):
        return self.rank == other.rank

import random

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self.cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self.cards)

    def __str__(self): 
        """Returns the string representation of a deck."""
        result = ''
        for c in self.cards:
            result = self.result + str(c) + '\n'
        return result

def main():
    """A simple test."""
    deck = Deck()
    print("A new deck:")
    while len(deck) > 0:
        print(deck.deal())
    deck = Deck()
    deck.shuffle()
    print("A deck shuffled once:")
    while len(deck) > 0:
        print(deck.deal())

if __name__ == "__main__":
    main()
    
