from cards.deck import Deck
from cards.indexMaps import AlphaMap
from game.cardSet import CardSet

def testAlphaMap():
	mapping1 = AlphaMap()
	for i in range(52):
		c = 20 - len(mapping1.getText(i)[0])
		v = 5 - len(mapping1.getSave(i)[0])
		if i % 13 == 0: print()
		print(str(mapping1.getText(i)[0]) + " "*c + str(mapping1.getSave(i)[0]) + " "*v + str(mapping1.getRank(i)[0]))

def testHandRank():
	deck1 = Deck()
	mapping1 = AlphaMap()

	set = []
	for i in range(3):
		set.append(CardSet(5))

	set[0]._cards = mapping1.getFromSave(["S12", "S11", "S10", "S9", "S0"])
	set[1]._cards = mapping1.getFromSave(["S13", "S8", "S5", "S7", "S11"])
	set[2]._cards = mapping1.getFromSave(["H6", "S6", "C3", "H3", "C6"])

	for i in set:
		print(str(mapping1.getText(mapping1.sortByRank(i._cards))))

def testDraw():
	deck1 = Deck()
	mapping1 = AlphaMap()
	set = CardSet(5)
	while input("Draw? (y, n) ").lower() != "n":
		d = set.draw(deck1)
		if d != -1:
			print("You drew a " + str(mapping1.getText(d)[0]))
		else:
			print("You can't draw into a full set")
		print("You have a " + ", ".join(mapping1.getText(set._cards)) + " in your hand.")

def testSort():
	mapping1 = AlphaMap()
	deck1 = Deck()
	set = deck1.draw(52)
	print(mapping1.getRank(set))

	set = mapping1.sortByRank(set)

	print(mapping1.getRank(set))


################################################################################

testSort()
