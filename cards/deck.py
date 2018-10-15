import random

class DeckError(ValueError):
	"""Raise when there is an error with the deck"""

class Deck:
	def __draw(self):
		index = random.randint(0, self._card_count-1)
		inDeck = self.cardCount()
		if inDeck == 0:
			return -1
		while self.cardsInDeck[index] == False:
			index = random.randint(0, self._card_count-1)
		self.cardsInDeck[index] = False
		return index

	def draw(self, count=1):
		cards = []
		for i in range(count):
			cards.append(self.__draw())
		return cards

	def cardCount(self):
		inDeck = 0
		for i in self.cardsInDeck:
			if i == True:
				inDeck += 1
		return inDeck

	def __init__(self, cardCount=52):
		"""
		Sets up a basic deck of arbitrary length.
		cardCount: Amount of cards in the deck. Defaults to 52.
		"""
		self._card_count = cardCount
		self.cardsInDeck = []
		for i in range(self._card_count):
			self.cardsInDeck.append(True)
