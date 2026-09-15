class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = defaultdict(int)
        cnt2 = defaultdict(int)
        l = 0
        for s in s1:
            cnt1[s]+=1 
        
        for r in range(len(s2)):
            cnt2[s2[r]]+=1

            while r-l+1 > len(s1):
                cnt2[s2[l]]-=1
                if cnt2[s2[l]] == 0:
                    del cnt2[s2[l]]
                l+=1

            if cnt1 == cnt2:
                return True
        return False
        
