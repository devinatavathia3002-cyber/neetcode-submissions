class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # find pivot
        pivot = len(nums) - 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                pivot = (i - 1)
        
        l = 0
        r = len(nums) - 1

        if target >= nums[0] and target <= nums[pivot]:
            r = pivot
        else:
            l = pivot + 1
        
        while l <= r:
            m = ((r - l) // 2) + l
            print(m)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        

        return - 1
        
        