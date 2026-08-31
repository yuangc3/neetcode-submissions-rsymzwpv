class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for c in s:
            if c.isalnum():
                res += c.lower()
        l = 0 
        r = len(res)-1 
        while l <= r:
            if res[l] != res[r]:
                return False
            l+=1
            r-=1

        return True 
            
