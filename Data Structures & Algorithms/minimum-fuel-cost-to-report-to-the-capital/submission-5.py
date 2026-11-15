class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        res = 0
        n = len(roads) + 1
        # topo sort

        indegree = defaultdict(int)
        adj = defaultdict(list)

        q = deque()
        people = [1] * n

        # build adj + indegree list
        for road in roads:
            start, end = road
            adj[start].append(end)
            adj[end].append(start)
            indegree[start] += 1
            indegree[end] += 1
        
        for key in indegree:
            if indegree[key] == 1 and key != 0:
                q.append(key)
        
        while q:
            curr = q.popleft()
            res += math.ceil(people[curr] / seats)
            for node in adj[curr]:
                if node != 0:
                    indegree[node] -= 1
                    people[node] += people[curr]
                    if indegree[node] == 1:
                        q.append(node)
        return res