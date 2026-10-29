from collections import defaultdict
from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # map each node to its INGOING edges
        # count each nodes outgoing edges
        # 2: 0, 1: 1, 0: 1
        # 2: 1, 1: 0

        # for ingoing edges
        ingoing = defaultdict(list)

        # for ct outgoing edges
        outgoing = defaultdict(int)

        for i in range(len(graph)):
            outgoing[i] = 0
            if graph[i]:
                for val in graph[i]:
                    ingoing[val].append(i)
                    outgoing[i] += 1
        
        q = deque()
        res = []

        for node, val in outgoing.items():
            if val == 0:
                q.append(node)
                res.append(node)
        
        while q:
            node = q.popleft()
            for edge in ingoing[node]:
                outgoing[edge] -= 1
                if outgoing[edge] == 0:
                    q.append(edge)
                    res.append(edge)

        return sorted(res)
