class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # cooldown queue: [time, amountRemaining]
        queue = deque()

        # dict to get frequencies
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1

        # heap of frequency of each task
        maxHeap = []
        for freq in count.values():
            heapq.heappush(maxHeap, (-1) * freq)
        
        time = 0

        while queue or maxHeap:
            time += 1

            if maxHeap:
                amountLeftover = 1 + heapq.heappop(maxHeap)
                if amountLeftover != 0:
                    queue.append([time + n, amountLeftover])
            else:
                time = queue[0][0]

            if queue and queue[0][0] == time:
                heapq.heappush(maxHeap, queue.popleft()[1])
        
        return time
        

