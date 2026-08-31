class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = defaultdict(int)
        l = 0 
        res = 0 


        for i in range(len(s)):
            temp[s[i]]+=1

            while (i-l+1) - max(temp.values()) > k:
                temp[s[l]]-=1
                l+=1
            res = max(res, i-l+1)
        return res 