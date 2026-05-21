class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        index = 0 # interval index
        res = {} # map query to length
        minHeap = []

        for q in sorted(queries):
            
            while index < len(intervals) and intervals[index][0] <= q:
                l, r = intervals[index]
                heapq.heappush(minHeap, [r - l + 1, r])
                index += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            res[q] = minHeap[0][0] if minHeap else -1
        
        output = []
        for q in queries:
            output.append(res[q])
        
        return output