class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for query in queries:
            smallest = float("inf")
            for start, end in intervals:
                if start <= query <= end:
                    length = end - start + 1
                    smallest = min(smallest, length)

            if smallest == float("inf"):
                res.append(-1)
            else:
                res.append(smallest)

        return res