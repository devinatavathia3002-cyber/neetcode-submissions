class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # topological sort
        q = deque()
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for edge in edges:
            beg, end = edge
            adj[beg].append(end)
            adj[end].append(beg)
            indegree[beg] += 1
            indegree[end] += 1
        
        for val in indegree.keys():
            if indegree[val] == 1:
                q.append(val)
        
        while q:
            length = len(q)
            for i in range(length):
                curr = q.popleft()
                for val in adj[curr]:
                    indegree[val] -= 1
                    indegree[curr] -= 1
                    if indegree[val] == 1:
                        q.append(val)      
        
        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if indegree[u] >= 2 and indegree[v] >= 2:
                return edges[i]
        
        return edges[0]
