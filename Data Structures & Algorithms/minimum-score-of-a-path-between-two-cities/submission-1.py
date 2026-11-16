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
        visited.add(1)
        res = float("inf")

        while q:
            node, weight = q.popleft()
            for val in adj[node]:
                nodeVal, wght = val
                res = min(wght, res)
                if nodeVal not in visited:
                    q.append((nodeVal, wght))
                    visited.add(nodeVal)
        return res