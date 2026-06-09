class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        output = []

        def backtrack(total, sub, i):
            if total > target:
                return 
            elif total == target:
                output.append(sub.copy())
            else:
                for j in range(i, len(nums)):
                    sub.append(nums[j])
                    backtrack(total + nums[j], sub, j)
                    sub.pop()
            
        backtrack(0, [], 0)
        return output
