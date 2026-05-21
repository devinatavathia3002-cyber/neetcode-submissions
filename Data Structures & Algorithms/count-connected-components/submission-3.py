class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [False] * n
        counter = 0
        pre = defaultdict(list)
        for edge in edges:
            beg, end = edge
            pre[beg].append(end)
            pre[end].append(beg)

        def dfs(curr, parent):
            if visited[curr] == True:
                return
            visited[curr] = True
            for edge in pre[curr]:
                if edge == parent:
                    continue
                dfs(edge, curr)

        for num in range(n):
            if visited[num] == False:
                print(num)
                dfs(num, -1)
                counter += 1

        return counter