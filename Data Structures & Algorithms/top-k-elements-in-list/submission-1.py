class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        minHeap = [] # count, num
        # 1: 3, 2: 2, 3: 1

        for num in freq:
            count = freq[num]
            heapq.heappush(minHeap, (count, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        output = []
        while minHeap:
            freq, val = heapq.heappop(minHeap)
            output.append(val)

        return output

            
