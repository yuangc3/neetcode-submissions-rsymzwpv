"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True 
        intervals.sort(key = lambda x:x.start)
        last = intervals[0]

        for i in range(1, len(intervals)):
            current = intervals[i]
            if last.end <= current.start:
                last = current
            else:
                return False
        return True