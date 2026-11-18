class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # just find all nodes without an indegree??
        res = []
        indegree = defaultdict(int)
        for num in range(n):
            indegree[num] = 0
        for edge in edges:
            start, end = edge
            indegree[end] += 1
        
        for key in indegree:
            if indegree[key] == 0:
                res.append(key)
        
        return res