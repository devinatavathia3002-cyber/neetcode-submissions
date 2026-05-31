class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()
        res = []

        carry = 1

        for digit in digits:
            carry += digit
            if carry >= 10:
                carry = 1
                res.append(0)
            else:
                res.append(carry)
                carry = 0
        if carry == 1:
            res.append(carry)
        res.reverse()
        return res