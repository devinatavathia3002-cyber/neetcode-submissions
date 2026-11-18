from collections import defaultdict, deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # B, R, X -> X is uncolored, all nodes start with this
        n = len(graph)
        colors = ["X"] * n
        
        
        def bfs(start):
            q = deque()
            q.append(start)
            colors[start] = "R"

            while q:
                length = len(q)
                for i in range(length):
                    curr = q.popleft()
                    color = colors[curr]
                    for val in graph[curr]:
                        if colors[val] == "X":
                            q.append(val)
                            colors[val] = "R" if color != "R" else "B"
                        else:
                            if colors[val] == color:
                                return False


        for i in range(n):
            if colors[i] == "X":
                if bfs(i) == False:
                    return False

        return True


        
