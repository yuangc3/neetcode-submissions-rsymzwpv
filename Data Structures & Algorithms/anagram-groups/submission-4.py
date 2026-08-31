class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp = defaultdict(list)

        for v in strs:
            res = [0]*26
            for c in v:
                res[ord(c) - ord("a")]+=1
            temp[tuple(res)].append(v)
        return list(temp.values())