class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]

            # 不重叠
            if last[1] < current[0]:
                result.append(current)

            # 有重叠
            else:
                last[1] = max(last[1], current[1])

        return result