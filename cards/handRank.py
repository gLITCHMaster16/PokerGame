from enum import Enum
from cards.indexMaps import *

class ranks( Enum ):
    ROYAL_FLUSH = 9
    STRAIGHT_FLUSH = 8
    FOUR_OF = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0


class HandRank:
    def _getHandRank(self, hand):
        hand = self._IndexMapping.sortByRank(hand)
        hand = self._IndexMapping.getRank(hand)
        # print(hand)

        if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
            # All cards same suit
            n = hand[0][0]
            if hand[1][0] == n-1 and hand[2][0] == n-2 and hand[3][0] == n-3 and hand[4][0] == n-4:
                # Straight
                if n == 12:
                    return ranks.ROYAL_FLUSH, hand[0] # ROYAL FLUSH
                else:
                    return ranks.STRAIGHT_FLUSH, hand[0] # STRAIGHT FLUSH
            else:
                return ranks.FLUSH, hand[0] # FLUSH
        else:
            cc = []
            for i in hand:
                d = False
                for j in cc:
                    if i[0] == j[0]:
                        j[1] += 1
                        d = True
                if not d:
                    cc.append([i[0], 1])
            cc.sort(key=lambda cc: cc[1], reverse=True)
            if len(cc) < len(hand):
                # at least one set of at least two of n
                if cc[0][1] > 2:
                    if cc[0][1] == 4: # Four of card
                        if hand[0][0] == hand[1][0]:
                            return ranks.FOUR_OF, hand[0]
                        else:
                            return ranks.FOUR_OF, hand[1]
                    else:
                        if cc[1][1] > 1:
                            while hand[0][0] != hand[2][0]:
                                hand.pop(0)
                            return ranks.FULL_HOUSE, hand[0]
                        else:
                            while hand[0][0] != hand[1][0]:
                                hand.pop(0)
                            return ranks.THREE_OF, hand[0]
                elif cc[1][1] == 2:
                    return ranks.TWO_PAIR, hand[0]
                else:
                    return ranks.PAIR, hand[0]



            else: # No two of any N
                n = hand[0][0]
                if hand[1][0] == n-1 and hand[2][0] == n-2 and hand[3][0] == n-3 and hand[4][0] == n-4:
                    # Straight
                    return ranks.STRAIGHT, hand[0]
                else:
                    # High card
                    return ranks.HIGH_CARD, hand[0]

    def getHandRank(self, hand):
        """getHandRank"""
        if len(hand) < 5:
            return -1
        elif len(hand) > 5:
            return -1
        else:
            return self._getHandRank(hand)

    def __init__(self, IndexMapping:IndexMap):
        self._IndexMapping = IndexMapping
