class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newS = newInterval[0]
        newE = newInterval[1]

        for i in range(len(intervals)):
            start, end = intervals[i]
            if newE < start:
                res.append(newInterval)
                return res + intervals[i: len(intervals)]
            elif newS > end:
                res.append([start, end])
            else:
                newInterval[0] = min(newS, start)
                newInterval[1] = max(newE, end)
                newS, newE = newInterval

        res.append(newInterval)
        return res