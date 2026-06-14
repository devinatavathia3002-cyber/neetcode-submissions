class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        for course in prerequisites:
            crs, prereq = course
            adj[crs].append(prereq)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            adj[course] = []

            return True

        for i in range(numCourses):
            if dfs(i):
                continue
            return False
        
        return True