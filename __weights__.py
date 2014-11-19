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
from copy 		 import deepcopy
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
    def run_scenarios(self, num):
    	"""runs a number of scenarios of possible hand combinations 
    	given a certain deck configuration where there is a hand's worth
    	of cards removed.
    	num: integer number of trials
    	returns scen_distributions"""
    	mytrialhand= Hand()
    	self.shuffle()
    	self.move_cards(mytrialhand,13)
    	scen_distributions={}
    	for i in range(num):
      		theirtrialhand=Hand()
    		self.move_cards(theirtrialhand,13)
    		theirtrialhand.get_bid()
    		theirtrial
    		scen_distributions[deepcopy(theirtrialhand)]=theirtrialhand.bid
    		theirtrialhand.move_cards(mydeck,13)
    		mydeck.shuffle()

    	return scen_distributions




class Hand(Deck):
    """Represents a hand of playing cards."""
  
    def __init__(self, label='', d={},bid=None):
        self.cards = []
        self.label = label
        self.d     = {}
        self.bid   = 0
    def make_pmf(self):
    	for card in self.cards:
    		self.d[Card.rank_names[card.rank],Card.suit_names[card.suit]]=card.prob
    	#print self.d
    def get_bid(self):
    	self.make_pmf()
    	probs=self.d.values()
    	bid= 0
    	for val in probs:
    		bid=bid+val
    	self.bid=bid


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
	print mydeck.run_scenarios(1000)
	print("\n")