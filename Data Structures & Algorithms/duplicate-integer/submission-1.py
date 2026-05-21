class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         count = {}

         for val in nums:
            count[val] = count.get(val, 0) + 1
        
         for val in count.values():
            if val > 1:
                return True
        
         return False