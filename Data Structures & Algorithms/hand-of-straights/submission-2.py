class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for card in sorted(count):
            if count[card] > 0:
                group_count = count[card]

                for i in range(groupSize):
                    current = card + i

                    if count[current] < group_count:
                        return False

                    count[current] -= group_count

        return True