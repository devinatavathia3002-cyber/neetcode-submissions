class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        n = len(isConnected)
        
        def dfs(curr):
            for i in range(len(isConnected[curr - 1])):
                if isConnected[curr-1][i] == 1 and i + 1 not in visited:
                    visited.add(i + 1)
                    dfs(i + 1)

        for i in range(1, n + 1):
            if len(visited) == n:
                return res
            if i not in visited:
                dfs(i)
                res += 1
        return res