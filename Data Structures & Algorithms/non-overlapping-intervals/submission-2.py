class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        output = 0
        intervals.sort()
        lastElement = intervals[0]

        for i in range(1, len(intervals)):
            s, e = intervals[i]
            prevS, prevE = lastElement

            if prevE <= s:
                lastElement = [s, e]
            else:
                output += 1
                if prevE > e:
                    lastElement = [s, e]

        return output