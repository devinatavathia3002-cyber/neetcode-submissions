class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre = defaultdict(list)
        visited = set()
        for pair in prerequisites:
            past, post = pair
            pre[past].append(post)
        
        def dfs(num):
            nonlocal visited
            if pre[num] == []:
                return True
            if num in visited:
                return False
            
            visited.add(num)
            for prereq in pre[num]:
                if not dfs(prereq):
                    return False
            
            #visited.remove(num)
            pre[num] = []
            return True
            
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True