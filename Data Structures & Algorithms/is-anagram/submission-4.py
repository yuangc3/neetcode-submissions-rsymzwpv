class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = defaultdict(int)
        temp1 = defaultdict(int)
        for n in s:
            temp[n] += 1
        for h in t:
            temp1[h] += 1
        
        if temp == temp1:
            return True
        return False
        