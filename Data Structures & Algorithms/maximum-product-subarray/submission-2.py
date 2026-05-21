class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxi, mini = 1, 1

        for num in nums:
            if num == 0:
                maxi, mini = 1, 1
                continue
            res = max(res, maxi * num, mini * num, num)

            temp = maxi
            maxi = max(maxi * num, mini * num, num)
            mini = min(temp * num, mini * num, num)

        return res