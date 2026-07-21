class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        temp = defaultdict(int)
        if len(hand) % groupSize != 0:
            return False
        for n in hand:
            temp[n] += 1
        
        while len(temp) != 0:
            start = min(temp)
            for value in range(start, start + groupSize):
                if value in temp:
                    temp[value] -= 1
                else:
                    return False 
                if temp[value] == 0:
                    del temp[value]
        return True
