class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = set()
        total = 0
        minHeap = [[0, k]] # sum, value
        adj = defaultdict(list) # [time, endNode]
        for time in times:
            src, dest, weight = time
            adj[src].append([weight, dest])

        while minHeap and len(visited) < n:
            cumulative, val = heapq.heappop(minHeap)
            if val in visited:
                continue
            visited.add(val)
            total = cumulative

            for node in adj[val]:
                time, value = node
                heapq.heappush(minHeap, [cumulative + time, value])

        return total if len(visited) == n else -1

