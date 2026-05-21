class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # max heap
        maxHeap = []

        for x, y in points:
            distance = math.sqrt(((x - 0) * (x - 0)) + ((y - 0) * (y - 0)))
            if len(maxHeap) >= k:
                longest, popX, popY = maxHeap[0]
                if distance < abs(longest):
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, [(-1) * distance, x, y])
            else:
                heapq.heappush(maxHeap, [(-1) * distance, x, y])

        res = []
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        
        return res
