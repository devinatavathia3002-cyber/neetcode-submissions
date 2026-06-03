class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # freq = defaultdict(int)
        # length = len(nums)

        # for num in nums:
        #     freq[num] += 1
        
        # for num, count in freq.items():
        #     if count > length / 2:
        #         return num
        
        # return -1

        # voting algo

        count, res = 0, 0

        for num in nums:
            if count == 0:
                res = num
            if res == num:
                count += 1
            else:
                count -= 1
        
        return res