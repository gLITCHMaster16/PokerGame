import random
class Deck:
	def __draw(self):
		index = random.randint(0, 51)
		inDeck = 0
		for i in self.cardsInDeck:
			if i == True:
				inDeck += 1
		if inDeck == 0:
			return -1
		while self.cardsInDeck[index] == False:
			index = random.randint(0, 51)
		self.cardsInDeck[index] = False
		return index

	def draw(self, count=1):
		cards = []
		for i in range(count):
			cards.append(self.__draw())
		return cards

	def __init__(self):
		#print("init") # Traceback
		self.cardsInDeck = []
		for i in range(52):
			self.cardsInDeck.append(True)
