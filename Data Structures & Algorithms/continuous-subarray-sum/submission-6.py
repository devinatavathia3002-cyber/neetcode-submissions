class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = defaultdict(int)
        prefix[0] = -1
        currSum = 0

        for i, num in enumerate(nums):
            currSum += num
            leftover = currSum % k

            if leftover in prefix and (i - prefix[leftover]) > 1:
                return True
            
            if leftover not in prefix:
                prefix[leftover] = i

        return False