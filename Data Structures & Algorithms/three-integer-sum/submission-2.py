class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        output = []

        for i in range(len(nums)):

            if nums[i] > 0:
                break

            # account for duplicate start vals
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            target = (0 - nums[i])

            while l < r:
                add = nums[l] + nums[r]
                if add > target:
                    r -= 1
                elif add < target:
                    l += 1
                else:
                    subarr = [nums[i], nums[l], nums[r]]
                    output.append(subarr)
                    l += 1
                    r -= 1
                
                while l < r and nums[l] == nums[l - 1] and l != (i + 1):
                    l += 1

        return output
