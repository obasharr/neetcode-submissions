class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cardCounts = Counter(hand)

        while cardCounts:
            first = min(cardCounts)

            for i in range(groupSize):
                currentCard = first + i

                if currentCard not in cardCounts:
                    return False
                
                cardCounts[currentCard] -= 1

                if cardCounts[currentCard] == 0:
                    del cardCounts[currentCard]

        return True