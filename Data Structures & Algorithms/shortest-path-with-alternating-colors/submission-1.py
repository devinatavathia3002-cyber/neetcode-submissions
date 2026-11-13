class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = deque()
        adj = defaultdict(list)

        for edge in redEdges:
            num1, num2 = edge
            adj[num1].append((num2, "R"))
        
        for edge in blueEdges:
            num1, num2 = edge
            adj[num1].append((num2, "B"))
        
        q.append((0, "O"))
        visited = set()

        res = [-1] * n
        dist = 0

        while q:
            length = len(q)
            for i in range(length):
                num, color = q.popleft()
                if res[num] == -1:
                    res[num] = dist
                for edge in adj[num]:
                    edgeNum, edgeColor = edge
                    if edgeColor != color and edge not in visited:
                        visited.add(edge)
                        q.append(edge)
            dist += 1

        return res
