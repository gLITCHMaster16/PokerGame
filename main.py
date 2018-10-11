from cards.deck import Deck
from cards.indexMaps import AlphaMap

deck1 = Deck()
mapping1 = AlphaMap()

drawn = []
while input("Draw? (y, n) ").lower() != "n":
	d = deck1.draw()[0]
	print("You drew a " + str(mapping1.getText(d)[0]))
	drawn.append(d)
	print("You have a " + ", ".join(mapping1.getText(drawn)) + " in your hand.")
