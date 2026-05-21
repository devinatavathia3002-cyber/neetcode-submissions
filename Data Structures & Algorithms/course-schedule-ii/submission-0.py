class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        output = []
        taken = 0
        q = deque()
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for num in prerequisites:
            course, pre = num
            indegree[course] += 1
            adj[pre].append(course)
        
        for num in range(numCourses):
            if indegree[num] == 0:
                q.append(num)
        
        while q:
            length = len(q)
            for i in range(length):
                course = q.popleft()
                output.append(course)
                for num in adj[course]:
                    indegree[num] -= 1
                    if indegree[num] == 0:
                        q.append(num)
                adj[course] = []
                taken += 1

        return output if taken == numCourses else []