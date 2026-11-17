class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        visited = set()
        adj = defaultdict(list)
        n = len(isConnected)

        # step 1; setup adj list
        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1 and r != c:
                    adj[r + 1].append(c + 1)
        
        # step 2: perform dfs
        def dfs(curr):
            for num in adj[curr]:
                if num not in visited:
                    visited.add(num)
                    dfs(num)

        for i in range(1, n + 1):
            if len(visited) == n:
                return res
            if i not in visited:
                dfs(i)
                res += 1
        return res