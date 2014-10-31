"""This file contains code for use with the computational bayesian project
of Emily Guthrie and Cameron Anderson.

Write up of project: http://www.website.com
"""

"""This file contains class definitions for:

Deck: represents a deck of cards probability mass function (map from values to probs).

"""

from thinkbayes2 import Pmf
from thinkplot	 import *

class Deck(Pmf):
	"""represents a deck of cards' Pmf
	Values can be any hashable type; probabilities are floating-point.
	"""

