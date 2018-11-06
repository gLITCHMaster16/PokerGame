class HandRank:
    def _getHandRank(self, hand):
        hand = self._IndexMapping.sortByRank(hand)

        if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:
            # All cards same suit
            n = hand[0][0]
            if hand[1][0] == n-1 and hand[2][0] == n-2 and hand[3][0] == n-3 and hand[4][0] == n-4:
                # Straight
                if n == 12:
                    return 9, hand[0] # ROYAL FLUSH
                else:
                    return 8, hand[0] # STRAIGHT FLUSH
            else:
                return 5, hand[0] # FLUSH
        else:
            n = False
            for i in range(len(hand)):
                _hand = hand[:].pop(i)
                for j in _hand:
                    if j[0] == hand[i][0]:
                        n = hand[i]

            if n != False

    def getHandRank(self, hand):
        """getHandRank"""
        if len(hand) < 5:
            return -1
        else if len(hand) > 5:
        else:

    def __init__(self, IndexMapping:IndexMap):
        self._IndexMapping = IndexMapping
