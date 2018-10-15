from cards.indexMaps import IndexMap
from cards.deck import Deck

class CardSet:
    def __init__(self, indexMapping, maxCardsInSet:"The Max Amount of Cards that This Set Can Hold"=5):
        self._maxCards = maxCardsInSet
        self.indexMapping = indexMapping
        self._cards = []

    def drawToMax(self, deck: Deck):
        c = self._maxCards - len(self._cards)
        if c > 0:
            for i in deck.draw(c):
                self._cards.append(i)

    def getCardsInSet(self) -> []:
        return self._cards
