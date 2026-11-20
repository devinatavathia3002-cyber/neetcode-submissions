class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # return number of connected components
        visited = set()
        adj = defaultdict(list)
        res = 0

        # make adj list as always
        for edge in edges:
            start, end = edge
            adj[start].append(end)
            adj[end].append(start)
        
        def dfs(node, sub):
            if node in visited:
                return
            
            visited.add(node)
            sub.append(node)
            for val in adj[node]:
                dfs(val, sub)
            
            return sub
        

        for i in range(n):
            if i not in visited:
                allNodes = dfs(i, [])
                size = len(allNodes)
                flag = True
                for node in allNodes:
                    if len(adj[node]) != (size - 1):
                        flag = False
                if flag:
                    res += 1
        
        return res

