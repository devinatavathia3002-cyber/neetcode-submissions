class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        pre = defaultdict(list)
        for course in prerequisites:
            prereq, curr = course
            pre[curr].append(prereq)
        
        output = [False] * len(queries)
        
        def dfs(start, end, course, visited):
            if course in visited:
                return False
            if course == end:
                return True
            visited.add(course)
            for num in pre[course]:
                if dfs(start, end, num, visited):
                    return True
            return False
        
        for i in range(len(queries)):
            beg, end = queries[i]
            if dfs(end, beg, end, set()):
                output[i] = True
        
        return output