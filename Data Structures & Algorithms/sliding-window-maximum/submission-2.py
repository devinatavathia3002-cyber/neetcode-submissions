class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) <= 1:
            return nums

        output = []
        q = deque()

        l = 0
        r = 0

        while (r - l + 1) <= k:
            curr = nums[r]
            while q and curr > nums[q[-1]]:
                q.pop()
            q.append(r)

            r += 1
        
        r -= 1
        output.append(nums[q[0]])

        while r < len(nums) - 1:
            if q[0] == l:
                q.popleft()

            l += 1
            r += 1

            curr = nums[r]
            while q and curr > nums[q[-1]]:
                q.pop()
            q.append(r)

            output.append(nums[q[0]])

        return output
