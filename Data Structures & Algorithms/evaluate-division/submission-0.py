class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list) # a --> [b, a/b]
        for i, val in enumerate(equations):
            top, bottom = val
            adj[top].append([bottom, values[i]])
            adj[bottom].append([top, 1 / values[i]])
        
        output = []

        def bfs(src, tar):
            q = deque()
            visited = set()
            q.append((src, 1))

            while q:
                node, w = q.popleft()
                if node == tar:
                    return w
                visited.add(node)
                for nei in adj[node]:
                    if nei[0] in visited:
                        continue
                    visited.add(nei[0])
                    q.append((nei[0], nei[1] * w))
            return -1

        for q in queries:
            source, target = q
            if source not in adj.keys():
                output.append(-1)
            else:
                output.append(bfs(source, target))
        
        return output



