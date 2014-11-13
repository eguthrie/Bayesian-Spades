"""This file contains code for use with the computational bayesian project
of Emily Guthrie and Cameron Anderson. 
References and code: Allen Downey Think Bayesian and Think Python example code for card.py and thinkbayes2.py

Write up of project: http://www.website.com
"""

"""This file contains class definitions for:

Deck: represents a deck of cards probability mass function (map from values to probs).

"""

from thinkbayes2 import *
from thinkplot	 import *
import random


class Card(object):
    """Represents a standard playing card.
    
    Attributes:
      suit: integer 0-3
      rank: integer 1-13
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "King", "Queen", "Jack", "10",
    				"9","8","7","6","5","4","3","2"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        if suit == 3:
        	self.prob= (53-rank)/52.0
        else:
			self.prob= .25*((39-rank)/52.0)
    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck(object):
    """Represents a deck of cards.

    Attributes:
      cards: list of Card objects.
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def remove_card(self, card):
        """Removes a card from the deck."""
        self.cards.remove(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.

        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())

class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.d     = {}
    def make_pmf(self):
    	for card in self.cards:
    		self.d[card]=card.prob
    	print self.d


# def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
#    for ty in type(obj).mro():
#        if method_name in ty.__dict__:
#            return ty
#    return None
if __name__ == '__main__':
	mydeck=Deck()
	hand= Hand()
	mydeck.shuffle()
	mydeck.move_cards(hand,13)
	hand.make_pmf()
	print(hand.d)