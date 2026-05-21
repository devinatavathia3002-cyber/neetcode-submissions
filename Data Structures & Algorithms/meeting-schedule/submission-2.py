"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort(key = lambda x: x.start)
        prev = intervals[0]

        for i in range(1, len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            prevS, prevE = prev.start, prev.end

            if prevE <= start:
                prev = Interval(start, end)
            else:
                return False

        return True