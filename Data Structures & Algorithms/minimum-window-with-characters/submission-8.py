class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #x:1 y:1 z:1
        cnt2 = defaultdict(int)
        cnt = defaultdict(int)
        for z in t:
            cnt[z] += 1
        need = len(cnt)
        have = 0 
        l = 0
        res = [0, 0]
        resLen = float("inf")
        for r in range(len(s)):
            v = s[r]
            cnt2[v] += 1
            if v in cnt and cnt[v] == cnt2[v]:
                have += 1  
            while have == need:
                if resLen > r-l + 1:
                    resLen = r-l+1
                    res = [l,r]
                cnt2[s[l]] -= 1
                if s[l] in cnt and cnt[s[l]] > cnt2[s[l]]:
                    have -=1
                l+=1 
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""


        

