class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValid(s, start, end):

            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            
            return True
        

        l = 0
        r = len(s) - 1
        skips = 1

        while l <= r:

            if s[l] != s[r] and skips > 0:
                if isValid(s, l + 1, r):
                    l += 1
                elif isValid(s, l, r - 1):
                    r -= 1
                else:
                    return False
                skips -= 1
            
            elif s[l] != s[r]:
                return False
            
            else:
                l += 1
                r -= 1
        
        return True