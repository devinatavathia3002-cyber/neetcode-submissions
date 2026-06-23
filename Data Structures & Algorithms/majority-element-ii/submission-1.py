class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = (len(nums) // 3) + 1
        # hashmap, sorting, voting algo 
        output = []

        ct1, ct2 = 0, 0
        num1, num2 = 0, 0

        for num in nums:
            if num == num1:
                ct1 += 1
            elif num == num2:
                ct2 += 1
            elif ct1 <= 0:
                num1 = num
                ct1 = 1
            elif ct2 <= 0:
                num2 = num
                ct2 = 1
            else:
                ct1 -= 1
                ct2 -= 1
        
        time1, time2 = 0, 0
        for num in nums:
            if num == num1:
                time1 += 1
            elif num == num2:
                time2 += 1

        if time1 >= times:
            output.append(num1)
        if time2 >= times:
            output.append(num2)

        return output