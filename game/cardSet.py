from cards.indexMaps import IndexMap
from cards.deck import Deck

class CardSet:
    def __init__(self, maxCardsInSet:"The Max Amount of Cards that This Set Can Hold"=5):
        self._maxCards = maxCardsInSet
        self._cards = []

    def drawToMax(self, deck:Deck):
        c = self._maxCards - len(self._cards)
        if c > 0:
            for i in deck.draw(c):
                self._cards.append(i)
        else:
            return -1

    def draw(self, deck:Deck):
        c = self._maxCards - len(self._cards)
        if c > 0:
            v = deck.draw()[0]
            if v != -1:
                self._cards.append(v)
                return v
            else:
                return -1
        else:
            return -1

    def getCardsInSet(self) -> []:
        return self._cards
