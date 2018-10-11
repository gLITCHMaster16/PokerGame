from cards.deck import Deck
from cards.indexMaps import AlphaMap
#from Deck import

deck1 = Deck()
mapping1 = AlphaMap()

drawn = deck1.draw(13)
for i in mapping1.getSave(drawn):
	print(i + ": " + str(mapping1.getFromSave(i)))
