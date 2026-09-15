class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = defaultdict(int)
        for z in t:
            count1[z]+=1
        
        counts = defaultdict(int)
        res = [0, 0]
        resLen = float('inf')
        l = 0 

        have = 0 
        need = len(count1)

        for r in range(len(s)):
            v = s[r]
            counts[v]+= 1
            if v in count1 and count1[v] == counts[v]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r-l + 1
                counts[s[l]]-=1
                if s[l] in count1 and count1[s[l]] > counts[s[l]]:
                    have -= 1
                l+=1
        
        l, r = res 
        return s[l:r+1] if resLen != float("inf") else ""
