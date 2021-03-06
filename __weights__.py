"""This file contains code for use with the computational bayesian project
of Emily Guthrie and Cameron Anderson. 
References and code: Allen Downey Think Bayesian and Think Python example code for card.py and thinkbayes2.py

Write up of project: http://www.website.com
"""

"""This file contains class definitions for:

Deck: represents a deck of cards 
Hand: represents a hand of cards

"""
import thinkbayes2
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

class Hand(Deck):
    """Represents a hand of playing cards."""
  
    def __init__(self, label=''):
        self.cards = []
        self.label = label
        self.bid   = 0

    def get_bid(self):
    	d=[]
    	bid=0
    	for card in self.cards:
    		d.append(card.prob)
    	for val in d:
    		bid=bid+val
    	return bid
    def update(self):
    	self.bid = self.get_bid()
class Scenarios(thinkbayes2.Pmf):
	"""PMF for scenarios of hands"""
	def Likelihood(self,data,hypo):
		guess = NormalPdf(hypo.bid-.5,3.0/5)  #normal 
		#thinkplot.Pdf(guess)
		#thinkplot.Show()
		return guess.Density(data)

	def Update(self, data):
		for hypo in self.Values():
			like = self.Likelihood(data, hypo)
			self.Mult(hypo, like)
		self.Normalize()


def run_scenarios(mydeck, theirbid, num):
    """runs a number of scenarios of possible hand combinations 
    given a certain deck configuration where there is a hand's worth
    of cards removed.
    num: integer number of trials
    returns scen_distributions"""
    mytrialhand= Hand()
    mydeck.shuffle()
    mydeck.move_cards(mytrialhand,13)
    scen=Scenarios()						#new pmf of scenarios
    for i in range(num):
    	theirtrialhand=Hand()				
    	mydeck.move_cards(theirtrialhand,13)
    	theirtrialhand.update()				#updates hand score attribute
    	scen.Set(deepcopy(theirtrialhand),1)
       	theirtrialhand.move_cards(mydeck,13)#resets the deck
    	mydeck.shuffle()
    scen.Update(theirbid)
    itms=[]
    for key, value in scen.d.items():
    	itms.append((value,key))			#sets up the list to sort by val
    										#rather than key
    return sorted(itms, reverse=True)[:5], mytrialhand


if __name__ == '__main__':
	mydeck=Deck()
	theirbid=5
	tophands, mytrialhand = run_scenarios(mydeck,theirbid,1000)
	print 'Their bid was ',theirbid, '\n My hand was:\n', mytrialhand, '\n\n Their most likely hands are '
	for pair in tophands:
		print '\n', pair[1], '\n Probability \n', pair[0], '\n\n'
#	print hands[0][1], '\n Prob = ', hands[0][0], '\n\n', hands[1][1], '\n Prob = ', hands[1][0], '\n\n', hands[2][1], '\n Prob = ', hands[2][0] 