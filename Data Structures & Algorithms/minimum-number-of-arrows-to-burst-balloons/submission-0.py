class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
       # first step, order by first val in subarr?
       # [1,6],[2,8],[7,12],[10,16]
       # compare second val of curr sub to min of next sub and see how long you can iterate/cover before starting over 

       res = 1
       points.sort()

       curr = points[0][1]
       for j in range(1, len(points)):
            if curr < points[j][0]:
                res += 1
                curr = points[j][1]
            else:
                curr = min(curr, points[j][1])
       return res