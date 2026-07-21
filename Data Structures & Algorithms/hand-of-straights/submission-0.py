from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        while count:
            start = min(count)

            for value in range(start, start + groupSize):
                if value not in count:
                    return False

                count[value] -= 1

                if count[value] == 0:
                    del count[value]

        return True