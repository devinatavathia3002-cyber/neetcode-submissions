class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # pass in: hashmap, index, currList
        res = []
        count = defaultdict(bool)
        for num in nums:
            count[num] = False

        def backtracking(mapping, curr):
            nonlocal res

            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for val in nums:
                if mapping[val] == True:
                    continue
                curr.append(val)
                mapping[val] = True
                backtracking(mapping, curr)
                curr.pop()
                mapping[val] = False
        

        backtracking(count, [])
        return res
