class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT, countS = defaultdict(int), defaultdict(int)

        for n in t:
            countT[n] += 1
        l = 0 
        have, need = 0, len(countT)

        res, resLen = [0, 0], float("inf")
        for r in range(len(s)):
            c = s[r]
            countS[c] += 1
            if c in countT and countT[c] == countS[c]:
                have += 1
            
            while have == need:
                if r-l+1 < resLen:
                    res = [l, r]
                    resLen = r-l + 1
                countS[s[l]]-=1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -=1
                
                l+= 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""