class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        def backtracking(index):
            nonlocal res
            nonlocal part

            if index >= len(s):
                res.append(part.copy())
                return
            
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    part.append(s[index: i + 1])
                    backtracking(i + 1)
                    part.pop()

        def isPalindrome(s, l ,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        backtracking(0)
        return res