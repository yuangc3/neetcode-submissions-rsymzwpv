class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0 
        intervals.sort(key = lambda x:x[0])
        last = intervals[0]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if last[1] <= current[0]:
                last = current
            else:
                res += 1
                if current[1] < last[1]:        
                    last = current
        return res