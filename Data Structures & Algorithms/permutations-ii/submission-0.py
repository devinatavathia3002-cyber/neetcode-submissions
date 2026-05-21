class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        res = []
        
        def backtracking(count, sub):
            nonlocal res
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            
            for val in count.keys():
                if count[val] > 0:
                    sub.append(val)
                    count[val] -= 1
                    backtracking(count, sub)
                    sub.pop()
                    count[val] += 1
        

        backtracking(count, [])
        return res
