class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in connections:
            x, y = edge
            adj[x].append((y, 0))
            adj[y].append((x, 1))
        
        q = deque()
        q.append(0)

        reversals = 0
        visited = set()

        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                visited.add(curr)
                for edge in adj[curr]:
                    node, val = edge
                    if node not in visited:
                        if val == 0:
                            reversals += 1
                        q.append(node)
        
        return reversals
