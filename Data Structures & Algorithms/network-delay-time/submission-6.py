class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = set()
        path = defaultdict(list)

        # from/to weight mapping
        for time in times:
            u, v, w = time
            path[u].append((v, w))
        
        minHeap = []
        t = 0

        heapq.heappush(minHeap, (0, k))

        while len(minHeap) > 0 and len(visited) < n:
            weight, curr = heapq.heappop(minHeap)
            if curr in visited:
                continue
            visited.add(curr)
            t = weight # cumulative weight

            for outgoing in path[curr]:
                end, w = outgoing
                if end not in visited:
                    heapq.heappush(minHeap, (weight + w, end))
                else:
                    continue

        return t if len(visited) == n else -1
        

