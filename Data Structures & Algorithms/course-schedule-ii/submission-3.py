class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = []

        adj = defaultdict(list)
        indegree = defaultdict(int)

        for mapping in prerequisites:
            crs, prereq = mapping
            adj[prereq].append(crs)
            indegree[crs] += 1
        
        for i in range(numCourses):
            if i not in indegree:
                indegree[i] = 0
        
        q = deque()
        for crs in indegree:
            if indegree[crs] == 0:
                q.append(crs)
        
        while q:
            crs = q.popleft()
            res.append(crs)

            for outgoing in adj[crs]:
                indegree[outgoing] -= 1
                if indegree[outgoing] == 0:
                    q.append(outgoing)

        if len(res) != numCourses:
            return []
        return res