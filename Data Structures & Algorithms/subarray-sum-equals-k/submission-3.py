class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        currSum = 0

        prefix = {0: 1}

        for num in nums:
            currSum += num

            leftover = currSum - k

            if leftover in prefix:
                res += prefix[leftover]
             
            prefix[currSum] = (prefix.get(currSum, 0)) + 1
        
        return res