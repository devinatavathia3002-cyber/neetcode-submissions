class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # with backtracking
        res = 0

        def backtracking(index, subset):
            nonlocal res
            xOR = 0
            for num in subset:
                 xOR ^= num
            res += xOR
            
            for j in range(index, len(nums)):
                subset.append(nums[j])
                backtracking(j + 1, subset)
                subset.pop()


        backtracking(0, [])
        return res