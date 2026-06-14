class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        output = []
        adj = defaultdict(list)
        count = defaultdict(int)
        for course in prerequisites:
            end, beg = course
            adj[end].append(beg)
            count[beg] += 1

        q = deque()
        for i in range(numCourses):
            if i not in count:
                q.append(i)

        while q:
            course = q.popleft()
            output.append(course)

            for prereq in adj[course]:
                count[prereq] -= 1
                if count[prereq] <= 0:
                    q.append(prereq)

        return output[::-1] if len(output) == numCourses else []