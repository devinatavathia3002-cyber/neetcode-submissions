class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        q = deque() # [amountLeftover, time]

        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        
        maxHeap = [-x for x in count.values()]
        heapq.heapify(maxHeap) # max heap only has vals

        time = 0

        while q or maxHeap:
            time += 1

            if len(maxHeap) > 0:
                leftover = 1 + heapq.heappop(maxHeap)
                if leftover != 0:
                    q.append([leftover, time + n])
            else:
                time = q[0][1]
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])


        return time