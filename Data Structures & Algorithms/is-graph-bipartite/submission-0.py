from collections import defaultdict, deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # B, R, X -> X is uncolored, all nodes start with this
        n = len(graph)
        colors = ["X"] * n

        # setup adjacency list as always
        adj = defaultdict(list)
        for j in range(len(graph)):
            start = j
            for end in graph[j]:
                adj[start].append(end)
                adj[end].append(start)
        
        
        def bfs(start):
            q = deque()
            q.append(start)
            colors[start] = "R"

            while q:
                length = len(q)
                print(q)
                for i in range(length):
                    curr = q.popleft()
                    color = colors[curr]
                    for val in adj[curr]:
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


        
