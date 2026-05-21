class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n == 1:
            return [0]
            
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for edge in edges:
            beg, end = edge
            adj[beg].append(end)
            adj[end].append(beg)
            indegree[beg] += 1
            indegree[end] += 1
        remaining = n

        q = deque()
        for num in indegree.keys():
            if indegree[num] == 1:
                q.append(num)
        
        while remaining > 2:
            size = len(q)
            remaining -= size
            for i in range(size):
                curr = q.popleft()
                for nei in adj[curr]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)

        return list(q)