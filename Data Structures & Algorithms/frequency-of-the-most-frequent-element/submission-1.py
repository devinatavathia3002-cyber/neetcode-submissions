class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        freq = 0
        r, l = len(nums) - 1, len(nums) - 1
        total = 0
        
        nums.sort()
        while l >= 0:
            total += nums[l]
            freq = max(freq, r - l)
            while ((nums[r] * (r - l + 1)) > total + k):
                total -= nums[r]
                r -= 1
            l -= 1

        freq = max(freq, r - l)
        return freq