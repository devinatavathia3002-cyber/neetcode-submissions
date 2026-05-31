class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # # iteration 1 solution
        # digits.reverse()
        # res = []

        # carry = 1

        # for digit in digits:
        #     carry += digit
        #     if carry >= 10:
        #         carry = 1
        #         res.append(0)
        #     else:
        #         res.append(carry)
        #         carry = 0

        # if carry == 1:
        #     res.append(carry)
        # res.reverse()
        # return res

        # iteraiton 2
        for i in range(len(digits) - 1, - 1, -1):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + digits