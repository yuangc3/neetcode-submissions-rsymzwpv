class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #n[i][1] > t[i][0] and n[i+1][0] > t[i][1]
        result = []
        for i in range(len(intervals)):
            current = intervals[i]
            #if new 完全在右边边
            if current[1] < newInterval[0]:
                result.append(current)
            elif newInterval[1] < current[0]:
                #完全new在左边边
                result.append(newInterval)
                return result + intervals[i:]
            else:
                #有重叠
                newInterval = [min(current[0], newInterval[0]), max(current[1], newInterval[1])]
        
        result.append(newInterval)
        return result 


