class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort
        # create a map

        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        
        # index = 0
        # for i in range(3):
        #     amt = count[i]
        #     while amt > 0:
        #         nums[index] = i
        #         index += 1
        #         amt -= 1
        
        # three pointer approach 
        if len(nums) < 2:
            return nums

        L = 0
        while nums[L] == 0 and L < len(nums) - 1:
            L += 1
        R = len(nums) - 1
        while nums[R] == 2 and R > 0:
            R -= 1
        i = L + 1
        
        while i <= R:
            if nums[i] == 0:
                nums[L], nums[i] = nums[i], nums[L]
                if nums[i] != 2:
                    i += 1
                while nums[L] == 0 and L < len(nums):
                    L += 1
            elif nums[i] == 2:
                nums[R], nums[i] = nums[i], nums[R]
                if nums[i] != 0:
                    i += 1
                while nums[R] == 2 and R >= 0:
                    R -= 1
            else:
                i += 1
    
    # [0,1,0,2,1,0,1,2,2]
    #  L   i         R
