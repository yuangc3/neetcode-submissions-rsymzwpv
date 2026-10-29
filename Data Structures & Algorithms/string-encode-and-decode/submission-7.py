class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res +=str(length) + "#"+s
        print(res)
        return res 
    # 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        res = []
        l = 0 
        while l < len(s):
            j = l
            while s[j] != "#":
                j+=1
            length = int(s[l:j])
            res.append(s[j+1:j+1+length])
            l = j+1+length
        return res
        




