class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = defaultdict(int)
        temp2 = defaultdict(int)

        for n in s:
            temp1[n] += 1
        for n in t:
            temp2[n] += 1
        
        if temp1 == temp2:
            return True
        return False 