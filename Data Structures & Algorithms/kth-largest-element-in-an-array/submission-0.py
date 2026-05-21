class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # minHeap

        kElements = []

        for num in nums:
            heapq.heappush(kElements, num)
            if len(kElements) > k:
                heapq.heappop(kElements)
        
        return heapq.heappop(kElements)
