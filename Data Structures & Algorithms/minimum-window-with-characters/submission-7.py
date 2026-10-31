class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)
        cnt2 = defaultdict(int)
        for c in t:
            cnt[c] += 1
        
        resLen = float("inf") 
        res = [0, 0]

        need = len(cnt)
        l = 0
        have = 0 
        for r in range(len(s)):
            v = s[r]
            cnt2[v] += 1

            if v in cnt and cnt2[v] == cnt[v]:
                have += 1
            
            while have == need:
                if resLen > r-l+1:
                    resLen = r-l + 1
                    res = [l, r]
                cnt2[s[l]] -= 1
                if s[l] in cnt2 and cnt[s[l]] > cnt2[s[l]]:
                    have -= 1
                l+=1
        l, r = res

        return s[l:r+1] if resLen != float("inf") else "" 




