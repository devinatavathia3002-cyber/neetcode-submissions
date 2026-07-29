class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        adj = defaultdict(list)

        for prereq in prerequisites:
            crs, before = prereq
            adj[crs].append(before)
            count[before] += 1

        q = deque()
        for i in range(numCourses):
            if i not in count:
                q.append(i)
        
        output = []
        while q:
            popped = q.pop()
            output.append(popped)
            for crs in adj[popped]:
                count[crs] -= 1
                if count[crs] == 0:
                    q.append(crs)

        return output[::-1] if len(output) == numCourses else []
