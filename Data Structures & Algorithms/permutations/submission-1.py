class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        mapping = defaultdict(bool)
        for num in nums:
            mapping[num] = False
        
        def backtrack(sub):
            if len(sub) == len(nums):
                output.append(sub)
                return
            
            for num in nums:
                if mapping[num]:
                    continue
                sub.append(num)
                mapping[num] = True
                backtrack(sub.copy())
                mapping[num] = False
                sub.pop()


        backtrack([])
        return output