class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        visited = set()
        up = defaultdict(list)

        for edge in edges:
            beg, end = edge
            up[beg].append(end)
            up[end].append(beg)
        
        def dfs(curr, parent):
            if curr in visited:
                return False
            visited.add(curr)
            for num in up[curr]:
                if num == parent:
                    continue
                if not dfs(num, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n 