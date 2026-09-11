class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for v in t:
            countT[v]+=1
        
        for z in s:
            countS[z]+=1
        
        print(countS)
        #print(countT)
        if countT == countS:
            return True
        return False 