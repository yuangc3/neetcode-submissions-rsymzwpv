class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        res = 0
        new = intervals[0]
        for i in range(1, len(intervals)):
            current = intervals[i]
            #如果不重叠
            if new[1] <= current[0]:
                new = current
            else: #重叠
                res += 1
                if current[1] < new[1]:
                    new = current
        return res 
        
