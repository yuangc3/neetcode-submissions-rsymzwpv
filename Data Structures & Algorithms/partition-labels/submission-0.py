class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #split into substring 
        #each letter apprear in at most one substring 
        last = {}

        for i, char in enumerate(s):
            last[char] = i
        

        result = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            end = max(end, last[char])

            if i == end:
                length = end -start + 1
                start = i+1
                result.append(length)
        return result
