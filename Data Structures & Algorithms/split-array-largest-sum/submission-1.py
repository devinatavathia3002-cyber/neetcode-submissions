class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # with backtracking, we have a number of buckets & sum we want to minimize

        # n = len(nums)
        
        # def backtrack(i, leftOver):
        #     if i >= n and leftOver == 0:
        #         return 0
        #     elif i >= n:
        #         return float("inf")
        #     elif leftOver == 0:
        #         return float("inf")
            
        #     else:
        #         minimum = float("inf")
        #         total = 0
        #         for j in range(i, n):
        #             curr = nums[j]
        #             total += curr
        #             minimum = min(minimum, max(total, backtrack(j + 1, leftOver - 1)))
            
        #     return minimum


        # return backtrack(0, k)

        # with binary search + greedy approach
        l, r = max(nums), sum(nums)
        res = r
        
        def isPossible(val):
            sub = 0
            total = 0

            for num in nums:
                total += num
                if total > val:
                    sub += 1
                    total = num
            
            return (sub + 1) <= k
        
        # first, binary search
        while l <= r:
            mid = ((r - l) // 2) + l
            if isPossible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1


        return res
