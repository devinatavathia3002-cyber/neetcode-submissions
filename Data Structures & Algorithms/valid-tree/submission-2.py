class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited = set()
        for edge in edges:
            s, e = edge
            adj[s].append(e)
            adj[e].append(s)
        

        def findLoop(v, parent):            
            if v in visited:
                return False
            
            visited.add(v)
            for edge in adj[v]:
                if edge == parent:
                    continue

                if findLoop(edge, v) == False:
                    return False
            
            return True

        return findLoop(0, -1) and len(visited) == n
