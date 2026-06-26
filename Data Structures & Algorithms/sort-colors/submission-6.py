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

        L = 0
        R = len(nums) - 1
        i = L
        
        while i <= R:
            if nums[i] == 0:
                nums[L], nums[i] = nums[i], nums[L]
                L += 1
                i += 1
            elif nums[i] == 2:
                nums[R], nums[i] = nums[i], nums[R]
                R -= 1
            else:
                i += 1
    
    # [0,1,0,2,1,0,1,2,2]
    #  L   i         R