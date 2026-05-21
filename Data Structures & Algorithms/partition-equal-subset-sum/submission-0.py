class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        dp = set()
        dp.add(0)
        target = total //2 

        for num in nums:
            newTarget = target - num
            if newTarget in dp:
                return True
            
            replica = dp.copy()
            for val in dp:
                replica.add(val)
                replica.add(val + num)
            dp = replica
        
        return False
        
        