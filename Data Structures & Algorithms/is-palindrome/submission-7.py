class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                string += c.lower()
        
        l, r = 0, len(string)-1
        while l < r:
            if string[l] != string[r]:
                return False
            l+=1
            r-=1
        return True



