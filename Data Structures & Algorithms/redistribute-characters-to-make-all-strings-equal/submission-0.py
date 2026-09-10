class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        temp = defaultdict(int)
        count = 0
        for s in words:

            for v in s:
                count += 1
                temp[v]+= 1
        
        for c in temp:
            if temp[c] % len(words) != 0:
                return False 
        return True 