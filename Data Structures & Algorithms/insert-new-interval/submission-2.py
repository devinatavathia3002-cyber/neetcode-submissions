class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        newS, newE = newInterval
        # 2,  5

        for i in range(len(intervals)):
            currS, currE = intervals[i]
            if newS > currE:
                res.append([currS, currE])
            elif newE < currS:
                res.append(newInterval)
                for j in range(i, len(intervals)):
                    res.append(intervals[j])
                return res
            else:
                newInterval[0] = min(newS, currS)
                newInterval[1] = max(newE, currE)
                newS, newE = newInterval

        res.append(newInterval)
        return res