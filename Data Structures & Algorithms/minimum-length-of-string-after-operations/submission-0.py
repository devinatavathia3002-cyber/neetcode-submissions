class Solution:
    def minimumLength(self, s: str) -> int:
        charArr = [0] * 26
        total = 0
        for char in s:
            charArr[ord(char) - ord('a')] += 1
        
        for val in charArr:
            if val:
                if val % 2 == 0:
                    total += 2
                else:
                    total += 1
        
        return total

