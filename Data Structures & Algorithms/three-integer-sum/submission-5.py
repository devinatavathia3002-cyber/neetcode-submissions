class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        last = float("-inf")

        for i in range(len(nums) - 2):
            curr = nums[i]
            if curr == last:
                continue

            target = 0 - curr

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r]
                if sum == target:
                    res.append([curr, nums[l], nums[r]])
                    lastl = nums[l]
                    l += 1
                    r -= 1

                    while nums[l] == lastl and l < r:
                        l += 1
                elif sum < target:
                    l += 1
                else:
                    r -= 1
            last = curr
    
        return res