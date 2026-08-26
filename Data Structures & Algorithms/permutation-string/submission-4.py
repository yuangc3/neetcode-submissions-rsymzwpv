class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        count1 = defaultdict(int)
        for n in s1:
            count1[n] += 1
        count = defaultdict(int)
        for r in range(len(s2)):
            count[s2[r]]+= 1
            while (r-l+1) > len(s1):
                count[s2[l]]-=1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l+= 1
            print(count)
            if count1 == count:
                return True
        return False 