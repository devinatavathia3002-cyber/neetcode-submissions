class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key = lambda x: x[0])
        output.append(intervals[0])

        for i in range(1, len(intervals)):
            start, end = output[-1]
            newS, newE = intervals[i]

            if end < newS:
                output.append([newS, newE])
            else:
                output[-1][0] = min(start, newS)
                output[-1][1] = max(end, newE)

        return output