class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        pal = []

        def dfs(index):
            nonlocal res

            if index == len(s):
                res.append(pal.copy())
                return
            
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    pal.append(s[index : i + 1])
                    dfs(i + 1)
                    pal.pop()


        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dfs(0)
        return res