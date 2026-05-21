class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visited = set()
        minHeap = [[0, k]] # weight, node
        adj = defaultdict(list)
        output = 0

        for time in times:
            src, dest, weight = time
            adj[src].append([weight, dest])
        
        while len(minHeap) > 0 and len(visited) < n:
            curr = heapq.heappop(minHeap)
            weight, node = curr
            if node in visited:
                continue
            output = weight
            visited.add(node)

            for nei in adj[node]:
                w, point = nei
                if point in visited:
                    continue
                heapq.heappush(minHeap, [w + weight, point])

        if len(visited) != n:
            return -1
        return output