class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bucket sort
        # create a map

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(3):
            amt = count[i]
            while amt > 0:
                nums[index] = i
                index += 1
                amt -= 1
        
