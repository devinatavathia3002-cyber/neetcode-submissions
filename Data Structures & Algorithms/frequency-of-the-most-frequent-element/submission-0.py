class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = 0
        r, l = len(nums) - 1, len(nums) - 1
        count = k
        
        nums.sort()
        while l >= 0:
            diff = nums[r] - nums[l]
            if diff <= count:
                count -= diff
                l -= 1
            else:
                freq = max(freq, r - l)
                r -= 1
                l = r
                count = k

        freq = max(freq, r - l)
        return freq