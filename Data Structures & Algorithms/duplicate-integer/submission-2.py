class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key in count:
            if count.get(key) > 1:
                return True
        
        return False
        