class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # prim's algo (optimal)

        res = 0
        visited = [False] * len(points)
        distances = [float("inf")] * len(points)
        edges = 0
        node = 0

        while edges < len(points) - 1:
            x, y = points[node]
            nextPoint = -1
            visited[node] = True

            for i in range(len(points)):
                if visited[i]:
                    continue
                xCord, yCord = points[i]
                distance = abs(xCord - points[node][0]) + abs(yCord - points[node][1])
                distances[i] = min(distances[i], distance)
                if nextPoint == -1 or distances[i] < distances[nextPoint]:
                    nextPoint = i

            node = nextPoint
            res += distances[nextPoint]
            edges += 1
        
        return res


