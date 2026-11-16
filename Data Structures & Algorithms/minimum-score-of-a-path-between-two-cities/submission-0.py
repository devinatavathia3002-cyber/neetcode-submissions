class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        q = deque()

        for road in roads:
            start, end, weight = road
            adj[start].append((end, weight))
            adj[end].append((start, weight))
        
        q.append((1, float("inf"))) #start, end
        visited.add((1, float("inf")))
        res = float("inf")

        while q:
            node, weight = q.popleft()
            res = min(weight, res)
            for val in adj[node]:
                nodeVal, wght = val
                if (nodeVal, wght) not in visited:
                    q.append((nodeVal, wght))
                    visited.add((nodeVal, wght))
        return res